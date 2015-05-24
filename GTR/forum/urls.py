# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views
#from views import LinkListView
#from views import LinkCreateView
#from views import LinkDetailView

urlpatterns = [

    # URL pattern for the UserUpdateView
    url(regex=r'^$', view=views.LinkListView.as_view(), name='forum'),
    url(regex=r'^create/$', view=views.LinkCreateView.as_view(), name='create'),
    #url(regex=r'^(?P<pk>\d+)/$', view=views.LinkDetailView.as_view(), name='link_detail'),
]

