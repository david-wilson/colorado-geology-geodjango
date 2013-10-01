from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
    TemplateView.as_view(template_name='units/nearby.html'),
    name='near-me'),
    url(r'^find/$', 'units.views.find_rocks', name='find-rocks'),
)
