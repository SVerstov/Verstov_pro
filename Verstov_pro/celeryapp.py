import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Verstov_pro.settings')

# install Celery
app = Celery('Verstov_pro')
# celery_app.config_from_object('Verstov_pro.settings', namespace='CELERY')
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()