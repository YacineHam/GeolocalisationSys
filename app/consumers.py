from app.models import Location
import json
from channels.generic.websocket import WebsocketConsumer
from .serializers import LocationSerializer
from .models import Location
from django.contrib.auth.models import AnonymousUser


class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print(self.scope['user'])
        if self.scope['user']==AnonymousUser:
            print("anonym")
            self.disconnect()
        else:
            pass


    def receive(self, text_data):
        location = json.loads(text_data)
        location = LocationSerializer(data=location)
        if location.is_valid():
            longitude=location.data['longitude']
            latitude =location.data['latitude']
            user = self.scope["user"]
            loc=Location(car=user,longitude=longitude,latitude=latitude)
            loc.save()
            print("location added")
            status={'status':'succes'}
            self.send(text_data=json.dumps(status))
        else:
            print(location.errors)
            self.send(text_data=json.dumps({'status':'error'}))
            
    def disconnect(self, close_code):
        self.close()
