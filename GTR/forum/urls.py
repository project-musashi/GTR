# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include

from . import views

urlpatterns = [

    # URL pattern for the UserUpdateView
    url(regex=r'^$', view=views.LinkListView.as_view(), name='forum'),
    url(regex=r'^create/$', view=views.LinkCreateView.as_view(), name='create'),
    url(regex=r'^(?P<pk>\d+)/$', view=views.LinkDetailView.as_view(), name='link_detail'),
    url(regex=r'^update/(?P<pk>\d+)/$', view=views.LinkUpdateView.as_view(), name='link_update'),
    url(regex=r'^delete/(?P<pk>\d+)/$', view=views.LinkDeleteView.as_view(), name='link_delete'),
    #url(r'^comments/', include('django_comments.urls'), name='comments'),
]

