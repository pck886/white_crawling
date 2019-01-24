# -*- coding:utf-8 -*-
# Author: chanlee(pck886@gmail.com)

from django.conf.urls import url

from .views import home

urlpatterns = [
    url(r'^$', home, name='index'),
]

