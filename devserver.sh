#!/bin/sh
source .venv/bin/activate
pip install -r 'mysite/requirements.txt'
python mysite/manage.py collectstatic --noinput
python mysite/manage.py makemigrations
python mysite/manage.py migrate
python mysite/manage.py test tests.user_test.user_create_test
python mysite/manage.py runserver $PORT
