# django_celery/celery.py

import os
from celery import Celery
from django.conf import settings



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodblog.settings")
app = Celery("foodblog")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)






# python -m celery -A foodblog worker -l info -P gevent  ---1 ci terminalda bu---
# python -m celery -A foodblog  beat -l info -S django  --- 2 ci terminalda bu---



# python -m celery -A foodblog worker --beat --scheduler django --loglevel=info -P gevent