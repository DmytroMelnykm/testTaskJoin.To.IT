#!/usr/bin/env sh

source venv/bin/activate

gunicorn service.wsgi