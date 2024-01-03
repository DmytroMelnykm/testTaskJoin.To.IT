from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max=255)
    organizer = models.CharField()

