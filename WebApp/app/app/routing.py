from django.urls import re_path
from Geolocalisation_System.AuthMiddleware import TokenAuthMiddleware
from .consumers import TestConsumer

websocket_urlpatterns = [
    re_path(r'ws/location/$', TestConsumer.as_asgi()),
]