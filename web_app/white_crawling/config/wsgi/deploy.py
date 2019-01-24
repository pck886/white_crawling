# -*- coding:utf-8 -*-
# Author: chanlee(pck886@gmail.com)

import os
import sys

from django.core.wsgi import get_wsgi_application

current_directory = os.path.dirname(__file__)
parent_directory = os.path.dirname(current_directory)
root_directory = os.path.dirname(parent_directory)

module_name = os.path.basename(current_directory)

sys.path.append(root_directory)
sys.path.append(parent_directory)
sys.path.append(current_directory)

os.environ['DJANGO_SETTINGS_MODULE'] = 'white_crawling.config.settings.deploy'

try:
    application = get_wsgi_application()
except Exception as err:
    print('\n[WSGI Error] %s' % err.__str__())

