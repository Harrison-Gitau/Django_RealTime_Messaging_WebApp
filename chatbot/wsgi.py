"""
WSGI config for chatbot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatbot.settings")

application = get_wsgi_application()

#Whitenoise 
# from whitenoise import WhiteNoise
# from chatbot import MyWSGIApp
# application = MyWSGIApp()
# application = WhiteNoise(application, root = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
# application.add_files(os.path.join(os.path.dirname(BASE_DIR), "static", "static")
