import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sheets_proj.settings')

app = Celery('sheets_proj')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
