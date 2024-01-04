from django.db import models
from django.contrib.auth import get_user_model


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class UserInvited(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    invited = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        unique_together = ["event", "invited"]
