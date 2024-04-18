#!/usr/bin/env bash
# exit on error
set -o errexit

python3 -m pip install --upgrade pip

pip install -r requirements.txt

#All AUTH
pip install django-allauth

python3 manage.py collectstatic --no-input
python3 manage.py migrate

