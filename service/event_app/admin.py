from django.contrib import admin
from .models import Event, UserInvited

# Register your models here.


admin.site.register([
    Event, 
    UserInvited
])
