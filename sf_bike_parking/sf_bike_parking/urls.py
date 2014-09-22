from django.conf.urls import patterns, include, url
from django.contrib import admin

from parkfinder import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<latitude>\d+)/(?P<longitude>\d+)/$', views.results, name='results'),
    url(r'^admin/', include(admin.site.urls)),
)
