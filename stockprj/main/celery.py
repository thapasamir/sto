from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab # scheduler
# default django settings

os.environ.setdefault('main','main.settings')
app = Celery('main')
app.conf.timezone = 'UTC'
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
