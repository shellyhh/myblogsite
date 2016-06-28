#-*- coding:utf8 -*-

from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from common import serialize_view

urlpatterns = [
    url(r'^(?P<app_name>[^/]*)/(?P<model_name>[^/]*)/$', serialize_view.ModelsViewList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
