from django.db import models

#from django.contrib.auth.models import User
from GTR.users.models import User
from django.db.models import Count
from django.core.urlresolvers import reverse

class LinkVoteCountManager(models.Manager):
    def get_queryset(self):
        return super(LinkVoteCountManager, self).get_queryset().annotate(
            votes=Count('vote')).order_by("-submitted_on","-votes")

class Link(models.Model):
    title = models.CharField("Headline", max_length=100)
    submitter = models.ForeignKey(User)
    submitted_on = models.DateTimeField(auto_now_add=True)
    rank_score = models.FloatField(default=0.0)
    url = models.URLField("URL", max_length=250, blank=True)
    self_description = models.TextField("Self description", blank=True)
    description = models.TextField(blank=True)
    with_votes = LinkVoteCountManager()
    objects = models.Manager() #default manager
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("forum:link_detail", kwargs={"pk": str(self.id)})

class Vote(models.Model):
    voter = models.ForeignKey(User)
    link = models.ForeignKey(Link)

    def __unicode__(self):
        return "%s upvoted %s" % (self.voter.username, self.link.title)

