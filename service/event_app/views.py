from .sereilizers import EventSerializer, UserInvitedSerializer
from .models import Event, UserInvited
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer


class UserInvitedViewSet(ModelViewSet):
    queryset = UserInvited.objects.all()
    serializer_class = UserInvitedSerializer
