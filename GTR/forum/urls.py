# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from GTR.forum.views import LinkListView

urlpatterns = [

    # URL pattern for the UserUpdateView
    url(regex=r'^$', view=LinkListView.as_view(), name='forum'),

]

