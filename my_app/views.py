from django.shortcuts import render
from .serializers import *
from .models import *
from .permissions import *
from rest_framework.viewsets import ModelViewSet

class Tour_classViewSet(ModelViewSet):
    queryset = Tour_class.objects.all()
    serializer_class = Tour_classSerializer
    permission_classes = [CustomPermission]

class TourViewSet(ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [CustomPermission]
    