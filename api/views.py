from django.shortcuts import render
from rest_framework import viewsets
from meetups.models import Location
from api.serializers import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer