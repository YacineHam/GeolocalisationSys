from .models import Location
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Location
        fields = ['car','longitude','latitude']
        
        
        def create(self, validated_data):
            return Location.objects.create(**validated_data)    
