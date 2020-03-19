from django.urls import path

from .consumers import GalConsumer

websocket_urlpatterns = [
    path("ws/gal/", GalConsumer),
]
