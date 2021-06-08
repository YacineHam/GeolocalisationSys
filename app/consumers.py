from app.models import Location
import json
from channels.generic.websocket import WebsocketConsumer
from .serializers import LocationSerializer
from .models import Location

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        print(text_data)
        location = json.loads(text_data)
        location = LocationSerializer(data=location)
       
        print(type(location))
        print(type(location.initial_data))
        if location.is_valid():
            location.save()
            status={'status':'succes'}
            self.send(text_data=json.dumps(status))
        else:
            print(location.errors)
            self.send(text_data=json.dumps({'status':'error'}))