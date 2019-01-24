#!/usr/bin/env bash

sudo systemctl daemon-reload
sudo systemctl stop uwsgi
sudo systemctl start uwsgi
sudo systemctl status uwsgi