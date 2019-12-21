#!/bin/bash
# pipenv shell

case $1 in
  dev)
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver --settings=onw.settings.dev 0.0.0.0:8000
    ;;
  prod)
    python manage.py collectstatic --noinput
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver --settings=onw.settings.prod 0.0.0.0:8000
    ;;
esac
