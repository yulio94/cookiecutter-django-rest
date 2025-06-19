"""Production settings."""

from .base import *  # NOQA
from decouple import config

SECRET_KEY = config("SECRET_KEY")
ALLOW_HOSTS = config("ALLOW_HOSTS", cast=list)

# Database
DATABASES["default"] = config("DATABASE_URL")
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = config("CONN_MAX_AGE", default=60, cast=int)  # NOQA

# Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,
        },
    }
}

# Security
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = config("SECURE_REDIRECT", default=True, cast=bool)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", default=60, cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config(
    "SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True, cast=bool
)
SECURE_HSTS_PRELOAD = config("SECURE_HSTS_PRELOAD", default=True, cast=bool)
SECURE_CONTENT_TYPE_NOSNIFF = config(
    "SECURE_CONTENT_TYPE_NOSNIFF", default=True, cast=bool
)

# Storage
INSTALLED_APPS += ["storages"]
AWS_STORAGE_BUCKET_NAME = config("DJANGO_AWS_STORAGE_BUCKET_NAME")
AWS_QUERYSTRING_AUTH = False
_AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate",
}

# Media
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/"

# Static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Templates
TEMPLATES[0]["OPTIONS"]["loaders"] = [  # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    ),
]

# Email
DEFAULT_FROM_EMAIL = config("DJANGO_DEFAULT_FROM_EMAIL")
SERVER_EMAIL = config("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
EMAIL_SUBJECT_PREFIX = config("DJANGO_EMAIL_SUBJECT_PREFIX")

# Admin
ADMIN_URL = config("DJANGO_ADMIN_URL")

# Anymail (Mailgun)
INSTALLED_APPS += ["anymail"]  # noqa F405
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
ANYMAIL = {
    "MAILGUN_API_KEY": config("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": config("MAILGUN_DOMAIN"),
}

# Gunicorn
INSTALLED_APPS += ["gunicorn"]  # noqa F405

# WhiteNoise
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")  # noqa F405

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        },
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}
