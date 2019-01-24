# -*- coding: utf-8 -*-
# Author: chanlee(pck886@gmail.com)

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class CrawlingData(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(null=True, default='', verbose_name='제목')
    date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    url = models.TextField(null=True, default='', verbose_name='링크')
    source = models.TextField(null=True, default='', verbose_name='source')
    content = models.TextField(null=True, default='', verbose_name='내용')
    company = models.TextField(null=True, default='', verbose_name='회사')
    isClean = models.TextField(null=True, default='', verbose_name='상태')
    author = models.TextField(null=True, default='', verbose_name='권한')
    link = models.TextField(default='', verbose_name='수집링크')
    search_word = models.TextField(default='', verbose_name='검색어')
    img_url = models.TextField(null=True, default='', verbose_name='이미지링크')
    data_url = models.TextField(null=True, default='', verbose_name='데이터링크')
    data_a = models.TextField(null=True, default='', verbose_name='데이터A')
    data_b = models.TextField(null=True, default='', verbose_name='데이터B')
    data_c = models.TextField(null=True, default='', verbose_name='데이터C')
    data_d = models.TextField(null=True, default='', verbose_name='데이터D')
    data_key = models.TextField(null=True, default='', verbose_name='데이터 키')
    visit_id = models.TextField(null=True, default='', verbose_name='방문ID')
    visit_status = models.TextField(null=True, default='', verbose_name='방문상태')
    published_date = models.DateTimeField(auto_now=True, verbose_name='컨텐츠 등록일')

    class Meta:
        ordering = ('published_date',)
        get_latest_by = ('published_date',)
        verbose_name_plural = 'Web Crawling Data'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.links