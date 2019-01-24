#!/usr/bin/env bash
sudo cp nginx.conf /etc/nginx/nginx.conf
sudo cp my_nginx.conf /etc/nginx/sites-available/
sudo cp uwsgi_params /etc/nginx/uwsgi_params