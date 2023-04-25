"""
ASGI config for g6api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
# from channels.auth import AuthMiddlewareStack <= # need to test it

from chatv1.consumers import TokenAuthConsumer
from chatv1.middlewares import TokenAuthMiddleWare

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'g6api.settings')

application = ProtocolTypeRouter({
  
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddleWare(
      AllowedHostsOriginValidator(
          URLRouter(
          [path("ws/socket-chat/", TokenAuthConsumer.as_asgi())]
          )
      )
    )

})
