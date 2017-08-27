from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# Set the Default Django Settings module for the Celery Program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')

# Using a string here means the worker will not have to
# pickle the object when using Windows
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)