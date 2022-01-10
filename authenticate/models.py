from django import forms
from django.core import validators
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import related
from django.db.models.fields.related import ManyToManyField
from django.forms import widgets
from django.forms.models import ModelForm
from django.contrib.auth.models import User 



class MyClubUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to = "images/profile/")
    credit = models.PositiveBigIntegerField(default=5, validators = [MaxValueValidator(15),MinValueValidator(0) ])
    onholdcredit = models.PositiveIntegerField(default=0, validators = [MaxValueValidator(15), MinValueValidator(0)])

    def __str__(self):
        return str(self.user)

class Service(models.Model):
    name = models.CharField('Service Name', max_length=120)
    date = models.DateField('Service Date', blank=True, null = True)
    time = models.TimeField(default='12:00')
    description=models.TextField()
    venue = models.CharField('Venue Name', max_length=120)
    credit = models.PositiveIntegerField()
    service_picture = models.ImageField(null=True, blank=True)
    provider = models.ForeignKey(User,default="", on_delete=models.CASCADE, related_name='service_provider')
    applied_ones = models.ManyToManyField(User,default="", blank=True, related_name='service_applied_ones')
    attendees = models.ManyToManyField(User,default="", blank=True, related_name='service_attendees')
    others = models.ManyToManyField(User, default="", blank=True, related_name='service_others')
    owner = models.IntegerField("Service Owner", blank=False, default = 1) 
    service_picture = models.ImageField(null=True, blank=True, upload_to = "images/")


    ChoicesForService = ((1,'Open'),(2,'Closed'),(3,'Done'))
    status = models.PositiveIntegerField(choices=ChoicesForService, default = 1)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    date = models.DateField('Event Date', blank=True, null = True)
    time = models.TimeField(default='12:00')
    description=models.TextField()
    venue = models.CharField('Venue Name', max_length=120)
    credit = models.PositiveIntegerField(default=0)
    service_picture = models.ImageField(null=True, blank=True)
    provider = models.ForeignKey(User,default="", null=True, on_delete=models.SET_NULL, related_name='event_provider')
    applied_ones = models.ManyToManyField(User,default="", related_name='event_applied_ones')
    attendees = models.ManyToManyField(User,default="", blank=True, related_name='event_attendees')
    others = models.ManyToManyField(User, default="", blank=True, related_name='event_others')
    owner = models.IntegerField("Event Owner", blank=False, default = 1) 
    event_picture = models.ImageField(null=True, blank=True, upload_to = "images/")


    ChoicesForService = ((1,'Open'),(2,'Closed'),(3,'Done'))
    status = models.PositiveIntegerField(choices=ChoicesForService, default = 1)

    def __str__(self):
        return self.name


class Final_Event_Status(models.Model):
    user_final_status = models.ManyToManyField(User, default="", related_name='event_user_status')
    event_final_status = models.ManyToManyField(Service, default="", related_name='event_final_status')

    choices = ((1,'Applied'), (2,'Accepted'),(3,'Completed'), (4,'Not Completed'),(5,'Rejected'))
    user_final_status = models.PositiveIntegerField(choices=choices)


# Create your models here.

class Final_Service_Status(models.Model):
    user_final_status = models.ManyToManyField(User, default="", blank=True, related_name='service_user_status')
    service_final_status = models.ManyToManyField(Service, default="", related_name='service_final_status')

    choices = ((1,'Applied'), (2,'Accepted'),(3,'Completed'), (4,'Not Completed'),(5,'Rejected'))
    user_final_status = models.PositiveIntegerField(choices=choices)

class Measurement(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Distance from {self.location} to {self.destination} is {self.distance} km"