from app.models import Location
import json
from channels.generic.websocket import WebsocketConsumer
from .serializers import LocationSerializer
from .models import Location
from urllib.parse import parse_qs
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings
from .models import CustomUser,Location

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        self.close()

    def receive(self, text_data):
        location = json.loads(text_data)
        location = LocationSerializer(data=location)
        if location.is_valid():
            longitude=location.data['longitude']
            latitude =location.data['latitude']
            user = self.scope["user"]
            loc=Location(car=user,longitude=longitude,latitude=latitude)
            loc.save()
            status={'status':'succes'}
            self.send(text_data=json.dumps(status))
        else:
            print(location.errors)
            self.send(text_data=json.dumps({'status':'error'}))
 

#class TestConsumer(WebsocketConsumer):
#    def connect(self):
#        self.accept()
#            
#            
#            
#    def disconnect(self, close_code):
#        print("Disconxted")
#        self.close()
#
#    def receive(self, text_data):
#        location = json.loads(text_data)
#        location = LocationSerializer(data=location)
#        token = parse_qs(self.scope["query_string"].decode("utf8"))["token"][0]
#        try:
#            UntypedToken(token)
#            self.accept()
#            self.send(text_data=json.dumps({'status':'authenticated'}))
#            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
#            if location.is_valid():
#                longitude=location.data['longitude']
#                latitude =location.data['latitude']
#                user = CustomUser.objects.get(id=decoded_data["user_id"])
#                loc=Location(car=user,longitude=longitude,latitude=latitude)
#                loc.save()
#                status={'status':'succes'}
#                self.send(text_data=json.dumps(status))
#            else:
#                print("here")
#                print(location.errors)
#                self.send(text_data=json.dumps({'status':'error'}))
#        except (InvalidToken, TokenError) as e:
#            print("Non authenticated")
#            self.disconnect(500)
#       
#        