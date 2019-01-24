# -*- coding:utf-8 -*-
# Author: chanlee(pck886@gmail.com)

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")