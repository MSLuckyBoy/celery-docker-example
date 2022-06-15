from celery import Celery
from celery.schedules import crontab

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'crontab_every_5_minute': {
        'task': 'app.tasks.crontab_task',
        'schedule': crontab(minute='*/5'),
    },
}
