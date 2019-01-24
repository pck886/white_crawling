# -*- coding:utf-8 -*-
# Author: chanlee(pck886@gmail.com)


from . base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'white_crawling.config.wsgi.debug.application'

INSTALLED_APPS = [

    # Dajngo modules
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.postgres',
    'django.contrib.sitemaps',
    'django.contrib.sites',


    # Local apps
    'white_crawling.account',
    'white_crawling.news',

    # crawling apps
    'scrap'
]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'