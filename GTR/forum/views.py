from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Link, Vote
from django.views.generic.edit import CreateView
from .forms import LinkForm
from braces.views import LoginRequiredMixin
from django.views.generic import DetailView

class LinkListView(ListView):
    model = Link
    queryset = Link.with_votes.all()

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
