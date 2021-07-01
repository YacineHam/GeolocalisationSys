from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_current_location(request, id):
    car =CustomUser.objects.get(id=id)
    location = Location.objects.filter(car=car).last()
    return Response({"geometry": {"type": "Point", "coordinates": [location.longitude, location.latitude]}, "type": "Feature", "properties": {}})

def map(request):
    users = CustomUser.objects.filter(is_car=True)
    print(users)
    return render(request, 'map.html', {'users': users})

