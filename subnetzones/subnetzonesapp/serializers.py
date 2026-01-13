from rest_framework import serializers
from .models import subnetmodel

class subnetserializer(serializers.ModelSerializer):
    class Meta:
        model = subnetmodel
        fields = ['id', 'subnet', 'zone']

