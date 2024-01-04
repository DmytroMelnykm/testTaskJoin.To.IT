from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Event, UserInvited
from django.contrib.auth import get_user_model


class UserEventSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class EventSerializer(ModelSerializer):
    organizer = UserEventSerializer()

    class Meta:
        model = Event
        fields = '__all__'


class UserInvitedSerializer(ModelSerializer):
    event = PrimaryKeyRelatedField(queryset=Event.objects.all())
    invited = PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), many=True)


    class Meta:
        model = UserInvited
        fields = '__all__'
