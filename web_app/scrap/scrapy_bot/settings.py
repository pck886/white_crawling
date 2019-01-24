# -*- coding: utf-8 -*-
import sys

import os

BOT_NAME = 'scrapy_bot'

# 다운로더 미들웨어는 Scrapy의 요청 / 응답 처리를위한 프레임 워크입니다.
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 300,
    #'auto_website_scraper.middlewares.FilterResponses': 302,
}
# for chaching pourpose
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'  # using cache in file system
HTTPCACHE_ENABLED = True
HTTPCACHE_POLICY = 'scrapy.extensions.httpcache.DummyPolicy'
# HTTPCACHE_DIR='/scraper-cache/'

# for caching in db use 'scrapy.extensions.httpcache.DbmCacheStorage'

LOG_LEVEL = 'DEBUG'

FEED_EXPORT_ENCODING = 'utf-8'

# Optimization of scraper
# 쿠키 미들웨어를 사용할지 여부. 비활성화하면 웹 서버에 쿠키가 전송되지 않습니다.
COOKIES_ENABLED = True

# 광범위한 크롤링을 수행하는 경우 리디렉션을 저장하고 나중에 크롤링 할 때 사이트를 다시 방문 할 때 리디렉션을 해결하는 것이 일반적입니다.
REDIRECT_ENABLED = False

# Scrapy 다운로더가 수행 할 최대 동시 (즉, 동시) 요청 수입니다.
CONCURRENT_REQUESTS = 1

# 단일 도메인에 대해 수행 될 최대 동시 (즉, 동시) 요청 수입니다.
CONCURRENT_REQUESTS_PER_DOMAIN = 1

# 재시도 미들웨어 사용 여부.
RETRY_ENABLED = False

# 이것은 Scrapy 서버와 크롤링중인 웹 사이트의 부하를 기반으로 자동으로 크롤링 속도를 조절하는 확장 프로그램입니다.
AUTOTHROTTLE_ENABLED = True

# Twisted Reactor 스레드 풀 크기의 최대 한도입니다.
# 이것은 다양한 Scrapy 구성 요소에서 사용되는 일반적인 다목적 스레드 풀입니다.
# Threaded DNS Resolver, BlockingFeedStorage, S3FilesStore 등이 있습니다.
# 차단 IO 부족으로 문제가 발생하는 경우이 값을 늘리십시오.
REACTOR_THREADPOOL_MAXSIZE = 20

# 다운로더가 시간 초과되기까지 기다리는 시간 (초)입니다.
DOWNLOAD_TIMEOUT = 10

# DNS 인 메모리 캐시를 사용할지 여부.
DNSCACHE_ENABLED = True

# 동일한 웹 사이트에서 연속 된 페이지를 다운로드하기 전에 다운로더가 대기해야하는 시간 (초)입니다.
# 이 기능을 사용하면 서버를 너무 세게 치지 않도록 크롤링 속도를 조절할 수 있습니다.
# 10 진수가 지원됩니다.
DOWNLOAD_DELAY = 5

# 중복 요청을 탐지하고 필터링하는 데 사용되는 클래스입니다.
# DUPEFILTER_CLASS = 'auto_website_scraper.bloom_filter.BLOOMDupeFilter'

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

# crawler
DJANGO_PROJECT_PATH = '/home/chanlee/src/web_app'
DJANGO_SETTINGS_MODULE = 'white_crawling.config.settings.deploy'

sys.path.insert(0, DJANGO_PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE
BOT_NAME = 'spider_bot'

SPIDER_MODULES = ['scrapy_bot.spiders']

SPIDER_MIDDLEWARES = {
    'scrapy_bot.middlewares.RotateUserAgentMiddleware': 100
}

# 사용할 아이템 파이프 라인과 명령을 담고있는 dict.
# 주문 값은 임의적이지만 0-1000 범위에서 정의하는 것이 일반적입니다.
# 낮은 주문은 높은 주문 전에 처리됩니다.
ITEM_PIPELINES = {
    #'scrapy_bot.pipelines.ScrapyBotPipeline': 1000
    'scrapy_bot.pipelines.ScrapyBotPipeline': 200,
    'scrapy_bot.pipelines.DuplicatesPipeline': 100,
}

#USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"


# django 독립 실행 형 Python 스크립트 호출
# 외부에 있는 django INSTALLED_APPS라 호출 해줘야함
import django

django.setup()
