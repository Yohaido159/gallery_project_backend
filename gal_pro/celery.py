from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gal_pro.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

celery_app = Celery('gal_pro', include=["upload.tasks", "users.tasks"])
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()


@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
