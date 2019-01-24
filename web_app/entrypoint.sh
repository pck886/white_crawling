#!/bin/bash

if [ -z "$BASH_VERSION" ]; then
    exec bash "$0" "$@"
fi

# Wait postgres DB
dockerize -wait tcp://postgresdb:5432 -timeout 20s

# Collect static files
echo "[Collect static files]"
# python3 manage.py collectstatic --noinput

# Apply database migrations
echo "[Apply database migrations]"
# find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# find . -path "*/migrations/*.pyc"  -delete

# python3 manage.py collectstatic --noinput
# python3 manage.py syncdb --noinput
# python3 manage.py makemigrations
python3 manage.py migrate --noinput
# python3 manage.py migrate --fake
exec "$@"

# Django create admin
echo "[ADD DJANGO ADMIN]"
echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'cksrud10')" | python3 manage.py shell

# os system version
echo "[OS SYSTEM VERSION]"
uname -a

echo "[PYTHON VERSION]"
python --version

echo ""

ls -al

echo ""

ls -al /usr/local/lib/

echo ""

ls -al /var/log/uwsgi/

echo "[START UWSGI]"



# Start uwsgi
uwsgi --ini /web_app/.config_secret/uwsgi/deploy.ini


# Start scrapy
#echo "[BASH] Start Scrapy"

#cd scrap
#scrapy crawl scrapy_bot

# 임시
# sleep 100
