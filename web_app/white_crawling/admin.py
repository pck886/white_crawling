# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from news.models import CrawlingData


# Register your models here.
class CrawlingDataAdmin(admin.ModelAdmin):
    # inlines = [EquipmentListInline, ]
    list_display = ('id', 'title', 'url')
    list_display_links = ('id', 'title', )
    search_fields = ('title',)


admin.site.register(CrawlingData, CrawlingDataAdmin)
