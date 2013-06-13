# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from .views import PublicacioLlistaView

urlpatterns = patterns('',
    url(r'^$', PublicacioLlistaView.as_view(),
        name='publicacio-llista'),
)
