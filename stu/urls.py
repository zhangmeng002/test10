#!usr/bin/python
# -*- coding:utf-8 -*-
# __author = 'Bruce.张'

from django.urls import path, re_path
from . import views




urlpatterns = [
    path('query/', views.views_index),
    re_path('query/(?P<year>[0-9]{4})/(?P<month>\d{2})/', views.query1_view, {'name':'zhangsna'}),
    path('', views.index)


]