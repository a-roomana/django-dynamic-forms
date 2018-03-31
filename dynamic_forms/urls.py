# -*- coding: utf-8 -*-

from distutils.version import StrictVersion

from django import get_version

django_version = get_version()
if StrictVersion(django_version) >= StrictVersion('2.0'):
    from django.urls import re_path
else:
    from django.conf.urls import url as re_path

from .views import data_set_detail

app_name = 'dynamic_forms'

urlpatterns = [
    re_path(r'show/(?P<display_key>[a-zA-Z0-9]{24})/$', data_set_detail, name='data-set-detail'),
]
