#!/usr/bin/env bash

sudo systemctl stop nginx
sudo systemctl start nginx
sudo systemctl status nginx