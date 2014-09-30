from django.conf.urls import patterns, include, url
from django.contrib import admin

from parkfinder import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)

from <app> import settings
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )