from django.contrib import admin
from .models import Event, Venue
from .models import MyClubUser
from .models import Service

# Register your models here.

admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Service)
admin.site.register(Event)
