# -*- coding:utf-8 -*-
# Author: chanlee(pck886@gmail.com)

import sys
import os

current_directory = os.path.dirname(__file__)
parent_directory = os.path.dirname(current_directory)
root_directory = os.path.dirname(parent_directory)

module_name = os.path.basename(current_directory)

sys.path.append(root_directory)
sys.path.append(parent_directory)
sys.path.append(current_directory)

from .base import *

SECRET_KEY = config_secret_common['django']['secret_key']

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = True

ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'white_crawling.config.wsgi.deploy.application'

os.environ['APP_DATABASE_PASSWORD'] = 'I l1k3 us1nG p@assphrase @nd h@ck3r sTyl3'

INSTALLED_APPS = [

    # Dajngo modules
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.sitemaps',
    'django.contrib.sites',

    # Local apps
    'white_crawling.account',
    'white_crawling.news',

    # crawling apps
    'scrap'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.environ['APP_DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': 5433
    }
}

DEFAULT_FILE_STORAGE = 'ipfs_storage.InterPlanetaryFileSystemStorage'

IPFS_STORAGE_API_URL = 'http://localhost:5001/api/v0/'
IPFS_STORAGE_GATEWAY_URL = 'http://localhost:8080/ipfs/'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
