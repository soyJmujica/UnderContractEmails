#!/usr/bin/env bash
# exit on error

set -o errexit

poetry install
poetry add gunicorn
poetry add django
poetry add dj-database-url psycopg2-binary
poetry add 'whitenoise[brotli]'

python manage.py collectstatic --no-input
python manage.py migrate