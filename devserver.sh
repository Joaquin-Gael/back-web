#!/bin/sh
source .venv/bin/activate
pip install -r 'mysite/requirements.txt'
python3 mysite/manage.py collectstatic --noinput
python3 mysite/manage.py makemigrations
python3 mysite/manage.py migrate
python3 mysite/manage.py test tests.user_test.user_create_test
python3 mysite/manage.py runserver $PORT
