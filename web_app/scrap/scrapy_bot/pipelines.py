# -*- coding:utf-8 -*-
# Author: chanlee(pck886@gmail.com)
import json
import time

from scrapy.exporters import JsonItemExporter
from scrapy.exceptions import DropItem
from logger import logger

from white_crawling.news.models import CrawlingData
from utils.query import *


class ScrapyBotPipeline(object):

    def __init__(self, *a, **kw):
        src_json = kw.get('src_json') or 'resource/sample.json'
        self.MY_SETTINGS = json.load(open(src_json))
        self.srch_list = self.MY_SETTINGS['srch_list']

    def process_item(self, item, spider):
        try:
            valid = True
            item_model = item_to_model(item)

            obj, created = get_or_create(item_model)

            b_tit = next((s for s in self.srch_list if s in item['title']), None)
            b_con = next((s for s in self.srch_list if s in item['content']), None)

            if b_tit:
                item['search_word'] = b_tit
            elif b_con:
                item['search_word'] = b_con
            else:
                valid = False

            # for data in item:
            #
            #     item_row = CrawlingData.objects.filter(url=item['url']).first()
            #
            #     if item_row or (valid is False):
            #         valid = False
            #         raise DropItem("Missing %s of blogpost from %s" % (data, item['url']))

            if valid:
                logger.debug('=============== SAVE ITEM URL : %s ' % item['url'])
                logger.debug('=============== obj : %s ' % obj)
                update_model(obj, item_model)

            return item

        except TypeError:
            return item

        except Exception as e:

            if e.__str__() != '':
                logger.info('==================== [ERROR MESSAGE] %s ' % e.__str__())

            raise DropItem("Missing of blogpost from %s" % ( item['url']))

# ignore visited sites
class DuplicatesPipeline(object):

    def __init__(self):
        self.urls_seen = set()

    def process_item(self, item, spider):

        if item['url'] in self.urls_seen:
            raise DropItem("Duplicate item url found: %s" % item['url'])
        else:
            self.urls_seen.add(item['url'])
            return item


# export data into json
class JsonExportPipeline(object):

    def __init__(self):
        #log.start()
        #dispatcher.connect(self.spider_opened, signals.spider_opened)
        #dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.fjsons = {}

    def spider_opened(self, spider):
        fjson = open('output/%s_%s_items.json' % (spider.name, str(int(time.mktime(time.gmtime())))), 'wb')
        self.fjsons[spider] = fjson
        self.exporter = JsonItemExporter(fjson)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        fjson = self.fjsons.pop(spider)
        fjson.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
