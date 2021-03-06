from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Link, Vote
from django.views.generic.edit import CreateView
from .forms import LinkForm, VoteForm
from braces.views import LoginRequiredMixin
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
import json
from django.http import HttpResponse
import operator
from functools import reduce
from django.db.models import Q



class SearchListView(ListView):
    model = Link
    queryset = Link.with_votes.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)
        context["no_jumbotron"] = True
        context["search_results"] = True
        return context

    def get_queryset(self):
        result = super(SearchListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(description__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(self_description__icontains=q) for q in query_list))
            )
        return result

class LinkListView(ListView):
    model = Link
    queryset = Link.with_votes.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(LinkListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            voted = Vote.objects.filter(voter=self.request.user)
            links_in_page = [link.id for link in context["object_list"]]
            voted = voted.filter(link_id__in=links_in_page)
            voted = voted.values_list('link_id', flat=True)
            context["voted"] = voted

        context["no_jumbotron"] = True

        has_commented =[] # empty list
        for link in context["object_list"]:
            if (True == self.request.session.get('has_commented_' + str(link.id))): # pk is the object id
                has_commented.append(link.id)
        
        context["has_commented"] = has_commented

        return context

class LinkCreateView(LoginRequiredMixin, CreateView):
    model = Link
    form_class = LinkForm
    #template_name = "link_form.html"

    def form_valid(self, form):
        f = form.save(commit=False)
        f.rank_score = 0.0
        f.submitter = self.request.user
        f.save()

        return super(CreateView, self).form_valid(form)

class LinkDetailView(DetailView):

    model = Link
    def get_context_data(self, **kwargs):
        context = super(LinkDetailView, self).get_context_data(**kwargs)
        has_commented = self.request.session.get('has_commented_' + self.kwargs['pk']) # pk is the object id
        #print (self.kwargs['pk'])
        #print (has_commented) # if we don't setup the has_comment, the default value is None
        context["has_commented"] = has_commented
        context["no_jumbotron"] = True

        return context
        
def agree(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['obj_id']

    agree_count = 0

    if cat_id:
        cat = Link.objects.get(id=int(cat_id))
    if cat:
        if request.session.get('has_commented_' + cat_id, False):
            agree_count = cat.agree
        else:
            request.session['has_commented_' + cat_id] = True
            agree_count = cat.agree + 1
            cat.agree =  agree_count
            cat.save()
    return HttpResponse(agree_count)

def disagree(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['obj_id']

    disagree_count = 0

    if cat_id:
        cat = Link.objects.get(id=int(cat_id))
    if cat:
        if request.session.get('has_commented_' + cat_id, False):
            disagree_count = cat.disagree
        else:
            request.session['has_commented_' + cat_id] = True
            disagree_count = cat.disagree + 1
            cat.disagree =  disagree_count
            cat.save()
    return HttpResponse(disagree_count)

class LinkUpdateView(LoginRequiredMixin, UpdateView):
    model = Link
    form_class = LinkForm

class LinkDeleteView(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = reverse_lazy("forum:forum")

class JSONFormMixin(object):
    def create_response(self, vdict=dict(), valid_form=True):
        response = HttpResponse(json.dumps(vdict), content_type='application/json')
        response.status = 200 if valid_form else 500
        return response

class VoteFormBaseView(LoginRequiredMixin, FormView):
    form_class = VoteForm

    def create_response(self, vdict=dict(), valid_form=True):
        response = HttpResponse(json.dumps(vdict))
        response.status = 200 if valid_form else 500
        return response

    def form_valid(self, form):
        link = get_object_or_404(Link, pk=form.data["link"])
        user = self.request.user
        prev_votes = Vote.objects.filter(voter=user, link=link)
        has_voted = (len(prev_votes) > 0)

        ret = {"success": 1}
        if not has_voted:
            # add vote
            v = Vote.objects.create(voter=user, link=link)
            ret["voteobj"] = v.id
        else:
            # delete vote
            prev_votes[0].delete()
            ret["unvoted"] = 1
        return self.create_response(ret, True)

    def form_invalid(self, form):
        ret = {"success": 0, "form_errors": form.errors }
        return self.create_response(ret, False)

class VoteFormView(JSONFormMixin, VoteFormBaseView):
    pass

