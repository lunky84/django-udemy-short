from meetups.models import Location, Meetup
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'address']

class MeetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetup
        fields = ['id', 'title']