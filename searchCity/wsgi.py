"""
WSGI config for searchCity project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

import gunicorn
from django.core.wsgi import get_wsgi_application

import searchCity

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'searchCity.settings')

application = get_wsgi_application()

