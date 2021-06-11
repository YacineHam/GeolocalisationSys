from django.urls import re_path

from . import consumers
from Geolocalisation_System.AuthMiddleware import TokenAuthMiddleware

websocket_urlpatterns = [
    re_path(r'ws/test/$', consumers.TestConsumer.as_asgi()),
]