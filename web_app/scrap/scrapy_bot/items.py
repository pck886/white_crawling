# -*- coding:utf-8 -*-
# Author: chanlee(pck886@gmail.com)
from scrapy import Field
from scrapy_djangoitem import DjangoItem

from news.models import CrawlingData


class ScrapyScrapItem(DjangoItem):
    django_model = CrawlingData

    # define the fields for your item here like:
    # name = Field()
    title = Field()
    date = Field()
    url = Field()
    source = Field()
    content = Field()
    company = Field()
    isClean = Field()
    author = Field()
    link = Field()
    img_url = Field()
    data_url = Field()
    data_a = Field()
    data_b = Field()
    data_c = Field()
    data_d = Field()
    data_key = Field()
    visit_id = Field()
    visit_status = Field()


# class Page(DjangoItem):
#     django_model = CrawlingData
#
#     url = Field()
#     title = Field()
#     size = Field()
#     referer = Field()
#     newcookies = Field()
#     body = Field()


