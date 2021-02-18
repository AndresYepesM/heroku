"""
WSGI config for NSsocorro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NSsocorro.settings')

application = get_wsgi_application()


from NSsocorro import MyWSGIApp

application = MyWSGIApp()
application = WhiteNoise(application, root='/static/')
application.add_files('/static/', prefix='more-files/')