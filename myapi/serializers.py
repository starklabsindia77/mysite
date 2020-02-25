# serializers.py
from rest_framework import serializers

from .models import Driver

class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ('name', 'mobile', 'vehicle_type', 'password')
        