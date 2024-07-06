from rest_framework import serializers
from .models import *

class Tour_classSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour_class
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'
