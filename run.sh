#!/bin/bash

set -e

sudo docker-compose stop
sudo docker system prune -f
# sudo docker volume create --name=postgresdata || echo "================= Continue App ================="
# sudo docker volume rm whitecrawling_web_app || echo "================= Continue App ================="
docker-compose build --no-cache && docker-compose up -d && docker-compose logs -f -t --tail="all"

