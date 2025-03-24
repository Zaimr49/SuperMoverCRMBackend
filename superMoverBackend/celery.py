# project/celery.py
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superMoverBackend.settings')

app = Celery('superMoverBackend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-flk-bg-task-every-15-mins': {
        'task': 'crm.tasks.flk_leads_bg_task',
        'schedule': crontab(minute='*/1'),
    },
    'run-rea-bg-task-every-15-mins': {
        'task': 'crm.tasks.rea_leads_bg_task',
        'schedule': crontab(minute='*/1'),
    },
}
