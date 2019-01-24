#!/usr/bin/env bash

sudo docker-compose run app yes | python3 ./web_app/manage.py collectstatic --noinput
sudo docker-compose run app yes | python3 ./web_app/manage.py makemigrations
sudo docker-compose run app yes | python3 ./web_app/manage.py migrate

sudo docker-compose run cd ./web_app/scrap
sudo docker-compose run scrapy crawl scrapy_bot