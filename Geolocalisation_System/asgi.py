import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import app.routing
<<<<<<< HEAD
from .AuthMiddleware import TokenAuthMiddleware
=======
from .midleware import TokenAuthMiddleware
>>>>>>> 15f087598841a8525b0721909a1c45b7afceb18d

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddleware(
        URLRouter(
            app.routing.websocket_urlpatterns
        )
    ),
})