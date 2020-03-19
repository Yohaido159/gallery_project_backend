from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import upload.routing
import gallery.routing


from channels.security.websocket import OriginValidator


application = ProtocolTypeRouter({
    'websocket': OriginValidator(
        AuthMiddlewareStack(
            URLRouter(gallery.routing.websocket_urlpatterns)
        ),
        ["*"]
    )
})
