from django.contrib import admin
from django.db.models import fields
from .models import Event
from .models import MyClubUser
from .models import Service
from .models import Measurement
# Register your models here.


admin.site.register(Measurement)
admin.site.register(Service)
admin.site.register(Event)

@admin.register(MyClubUser)
class MyClubUserAdmin(admin.ModelAdmin):
    list_display = ('user','bio','credit','onholdcredit')
    search_fields = ('user',)

