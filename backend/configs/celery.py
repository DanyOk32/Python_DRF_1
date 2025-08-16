import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')
app = Celery('settings')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()
#періодична задача
app.conf.beat_schedule = {
    'send.spam_every_minutes':{
        'task': 'core.services.email_service.spam',
        'schedule': crontab(),
        # 'args': (),
    }
}
