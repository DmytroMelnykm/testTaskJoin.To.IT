from .sereilizers import (
    EventGetSerializer,
    EventCreateSerializer, 
    UserInvitedGetSerializer,
    UserInvitedCreateSerializer
)
from .models import Event, UserInvited
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

# Create your views here.


class EventViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all().order_by('-date')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'title': ['icontains'], 
        'organizer__username': ['icontains']
    }

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return EventGetSerializer
        return EventCreateSerializer


class UserInvitedViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserInvited.objects.all().order_by('-event')
    filterset_fields = {
        'event__title': ['icontains'], 
        'invited__organizer__username': ['icontains']
    }

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UserInvitedGetSerializer
        return UserInvitedCreateSerializer
    
    def perform_create(self, serializer):
        super().perform_create(serializer)
        if (id_obj := serializer.data.get('id')) is not None: 
            info_invite = UserInvited.objects.get(pk=id_obj)
            title_event = info_invite.event.title

            send_mail(
                subject=f"Invite to {title_event}",
                message=settings.MAIN_BODY_LIST_ACCEPT.format(
                    username=info_invite.invited.username,
                    title_event=title_event,
                ),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[info_invite.invited.username]
            )
    



