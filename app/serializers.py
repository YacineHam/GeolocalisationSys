from .models import Location
from rest_framework import serializers
from .models import CustomUser
from urllib.parse import parse_qs
from jwt import decode as jwt_decode
from django.conf import settings

class LocationSerializer(serializers.ModelSerializer):
    #car = serializers.SerializerMethodField('get_car')
                   
    #def get_car(self,obj):
    #        print("*********")
    #        print(type(obj))
    #        token = parse_qs(obj.scope["query_string"].decode("utf8"))["token"][0]
    #        decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    #        user = CustomUser.objects.get(id=decoded_data["user_id"])
    #        print("**************************")
    #        print(user)
    #        return user
    class Meta:
        model  = Location
        fields = ['longitude','latitude']

 
            
        def create(self, validated_data):
            return Location.objects.create(**validated_data)  
    


