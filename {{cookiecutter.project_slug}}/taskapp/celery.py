"""Celery app config"""

import os
from celery import Celery
from django.apps import apps, AppConfig
from django.conf import settings

if not settings.configured:
    # Set the default Django setttings module for 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

app = Celery('{{cookiecutter.project_slug}}')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


class CeleryAppConfig(AppConfig):
    name = '{{cookiecutter.project_slug}}.taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
