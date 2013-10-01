from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from .views import MapLayer
from .models import Unit

urlpatterns = patterns('',
    url(r'^$', MapLayer.as_view(model=Unit), name='units-json'),
    url(r'^nearby/$',
        TemplateView.as_view(template_name='units/nearby.html'),
        name='near-me'),
    url(r'^nearby/find/$', 'units.views.find_rocks', name='find-rocks'),
    )
