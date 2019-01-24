# -*- coding:utf-8 -*-
# Author: chanlee(pck886@gmail.com)

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
]

