"""Development settings."""

from .base import *  # NOQA
from decouple import config

# Base
DEBUG = True

# Security
SECRET_KEY = config(
    "DJANGO_SECRET_KEY",
    default="PB3aGvTmCkzaLGRAxDc3aMayKTPTDd5usT8gw4pCmKOk5AlJjh12pTrnNgQyOHCH",
)
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# Templates
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG

# Email
EMAIL_BACKEND = config(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

# django-extensions
INSTALLED_APPS += []

# Celery
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
