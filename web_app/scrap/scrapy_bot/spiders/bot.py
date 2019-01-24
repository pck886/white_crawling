# -*- coding:utf-8 -*-
# Author: chanlee(pck886@gmail.com)

import json
import os
import re

# Import nice CrawlSpider
from scrapy.exceptions import CloseSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from logger import logger


# Import our Items
from ..items import ScrapyScrapItem

# For Date Extraction
p1 = re.compile("\w+ \d+ \d+, \d+:\d+")
p2 = re.compile("\w+ \w+ \d+, \d+ \d+:\d+ \w+")


def get_date(text):
    if re.search(p1, text):
        return re.search(p1, text).group()
    elif re.search(p2, text):
        return re.search(p2, text).group()
    else:
        return text


class ScrapySpider(CrawlSpider):
    name = "scrapy_bot"
    rules = []

    def __init__(self, *a, **kw):
        src_json = kw.get('src_json') or 'resource/sample.json'

        # Dynamic loading from specified file
        self.MY_SETTINGS = json.load(open(src_json))

        self.allowed_domains = self.MY_SETTINGS['allowed_domains']
        self.start_urls = self.MY_SETTINGS["start_urls"]
        self.CONT_PATHS = self.MY_SETTINGS["paths"]

        for rule in self.MY_SETTINGS["rules"]:
            allow_r = ()
            if "allow" in rule.keys():
                allow_r = [a for a in rule["allow"]]

            deny_r = ()
            if "deny" in rule.keys():
                deny_r = [d for d in rule["deny"]]

            restrict_xpaths_r = ()
            if "restrict_xpaths" in rule.keys():
                restrict_xpaths_r = [rx for rx in rule["restrict_xpaths"]]

            ScrapySpider.rules.append(Rule(
                LinkExtractor(
                    allow=allow_r,
                    deny=deny_r,
                    #restrict_xpaths=restrict_xpaths_r,
                ),
                follow=rule["follow"],
                callback='parse_item'
            ))

        self.cookies_seen = set()

        self.OLD_URLS = []

        if not os.path.exists("output/"):
            os.makedirs("output/")

        try:
            fname = 'output/' + (src_json.split('/')[1].split('.')[0]) + "_visited.txt"
            f_urls = open(fname, 'r')
        except IOError:
            self.OLD_URLS = []
        else:
            self.OLD_URLS = [url.strip() for url in f_urls.readlines()]
            f_urls.close()
        finally:
            self.URLS_FILE = open(fname, 'a')

        super(ScrapySpider, self).__init__(*a, **kw)

    def parse_item(self, response):

        if str(response.url) not in self.OLD_URLS:
            logger.debug("Scraping: %s" % response.url)

            hxs = response

            item = ScrapyScrapItem()

            for article_path in self.CONT_PATHS["article"]:

                for article in hxs.xpath(article_path):

                    #logger.debug('================== article : %s' % article.extract())

                    item['url'] = response.url
                    item['source'] = self.MY_SETTINGS["source"]

                    item['link'] = None
                    for link_path in self.CONT_PATHS["link"]:
                        item['link'] = item['link'] or article.xpath(link_path).extract_first()

                    item['title'] = None
                    for title_path in self.CONT_PATHS["title"]:
                        item['title'] = item['title'] or article.xpath(title_path).extract_first()

                    item['date'] = None
                    for date_path in self.CONT_PATHS["date"]:
                        item['date'] = item['date'] or article.xpath(date_path).extract_first()

                    item['img_url'] = None
                    for img_path in self.CONT_PATHS['img']:
                        item['img_url'] = item['img_url'] or article.xpath(img_path).extract_first()

                    item['author'] = None
                    for author_path in self.CONT_PATHS['author']:
                        item['author'] = item['author'] or article.xpath(author_path).extract_first()

                    div = None
                    for div_path in self.CONT_PATHS["text"]:
                        div = div or article.xpath(div_path).extract_first()

                    text = div.split("[/caption]")

                    # Final item entry
                    item['date'] = get_date(item['date'])
                    item['content'] = ''.join(text[1]) if len(text) > 1 else ''.join(text)
                    item['company'] = self.MY_SETTINGS["company"]
                    item['isClean'] = False

                    yield item

            self.URLS_FILE.write(str(response.url) + '\n')


