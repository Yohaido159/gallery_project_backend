import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from django.core import serializers

from .models import Gallery
from django.db.models import Q


class GalConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        search_type = text_data_json["search"]
        if search_type != "":
            gal_names = Gallery.objects.all()
            result = gal_names.filter(
                Q(title__iexact=search_type) |
                Q(title__icontains=search_type) |
                Q(description__iexact=search_type) |
                Q(description__icontains=search_type)
            )
        else:
            result = ""

        data = serializers.serialize("json", result)
        self.send(text_data=json.dumps({
            "searchResult": data
        }))
