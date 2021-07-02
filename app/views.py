from typing import List, Type
from django.shortcuts import render
from rest_framework import response
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import timedelta
from django.utils import timezone
from base64 import b64decode,b64encode

from rest_framework.views import APIView
import rsa
from django.http import JsonResponse
from .models import CustomUser
from Geolocalisation_System.settings import pubKey,privateKey
from urllib.parse import parse_qs
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken
from jwt import decode as jwt_decode
from Geolocalisation_System import settings 



def map(request):
    users = CustomUser.objects.filter(is_car=True)
    return render(request, 'map.html', {'users': users})

@api_view(['GET'])
def get_current_location(request, id):
    car =CustomUser.objects.get(id=id)
    location = Location.objects.filter(car=car).last()
    return Response({"geometry": {"type": "Point", "coordinates": [location.longitude, location.latitude]}, "type": "Feature", "properties": {}})

def get_history(request, id):
    car =CustomUser.objects.get(id=id)
    locations = Location.objects.filter(car=car).order_by("timestamp")
    locs = list()
    for location in locations :
        locs.append([location.longitude, location.latitude])
    return render(request, 'history.html', {'locations': locs, 'car':car, 'center': locs[-1]})



#Add Retruive Public Key based On jwt
class StoreAesKey(APIView):

    def post(self,request):
        aes_crypted=request.data['aes_key']
        token = request.data['access']
        try:
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            return JsonResponse({'note':'invalid token'})
        else:
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = CustomUser.objects.get(id=decoded_data["user_id"])
            aes_key = rsa.decrypt(b64decode(aes_crypted), privateKey).decode()
            user.aes_key=aes_key
            user.save()
        return JsonResponse({'succes':'succes'})
    
class GetRsaKey(APIView):

    
    def post(self,request): 
        token = request.data['access']
        try:
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            return JsonResponse({'note':'invalid token'})
        else:        
            return JsonResponse({'pubkey':{'n':str(pubKey.n),'e':str(pubKey.e)}})
    
    

    
