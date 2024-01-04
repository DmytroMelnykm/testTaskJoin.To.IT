from rest_framework.serializers import ModelSerializer
from .models import Event, UserInvited
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']


class EventGetSerializer(ModelSerializer):
    organizer = UserSerializer()

    class Meta:
        model = Event
        fields = '__all__'


class EventCreateSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class UserInvitedGetSerializer(ModelSerializer):
    event = EventGetSerializer()
    invited = UserSerializer()

    class Meta:
        model = UserInvited
        fields = '__all__'
    

class UserInvitedCreateSerializer(ModelSerializer):

    class Meta:
        model = UserInvited
        fields = '__all__'
