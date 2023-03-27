import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject1.settings')

app = Celery('myproject1')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'send_mail_monday_8am': {
        'task': 'board.tasks.send_mail_monday_8am',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}
