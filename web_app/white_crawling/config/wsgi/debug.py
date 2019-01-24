# -*- coding:utf-8 -*-
# Author: chanlee(pck886@gmail.com)

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "white_crawling.config.settings.debug")

application = get_wsgi_application()