# backend/asgi.py
import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Lissnify.settings')

# Configure Django settings before importing anything else
django.setup()

# Now import Django-dependent modules
from chat_api.middleware import JWTAuthMiddleware
import chat_api.routing
import notification_api.routing

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": JWTAuthMiddleware(
        URLRouter(
            chat_api.routing.websocket_urlpatterns + 
            notification_api.routing.websocket_urlpatterns
        )
    ),
})
