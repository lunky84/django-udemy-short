from django.shortcuts import render
from rest_framework import viewsets
from meetups.models import Location, Meetup
from api.serializers import LocationSerializer, MeetupSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class MeetupAuthenticatedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = Meetup.objects.all()
        serializer = MeetupSerializer(queryset, many=True)

        return Response(serializer.data)