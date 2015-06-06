# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

# generate 

from django.contrib.sitemaps import GenericSitemap
from GTR.forum.models import Link
from django.contrib.sitemaps import Sitemap

class MainSitemap( Sitemap ):
 
  def items(self):
    return [self]

  location = "/"
  changefreq = "monthly"
  priority = "1"

Link_dict = {
    'queryset': Link.objects.all(),
    'date_field': 'submitted_on',
}


sitemaps = {
    'link': GenericSitemap(Link_dict, priority=0.8),
    'main_page' : MainSitemap,
}

urlpatterns = [
    url(r'^home/$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # Django Admin
    url(r'^admin_musashi/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("GTR.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here

    url(r'^',  include("GTR.forum.urls", namespace="forum")),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    ]
