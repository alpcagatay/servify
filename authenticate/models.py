from django import forms
from django.db import models
import datetime
from django.forms import widgets
from django.forms.models import ModelForm


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.TextField('Venue Address')
    
    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name = models.CharField('First Name', max_length=120)
    last_name = models.CharField('Last Name', max_length=120)
    username = models.CharField('Username', max_length=120)


class Service(models.Model):
    name = models.CharField('Service Name', max_length=120)
    date = models.DateField('Service Date', blank=True, null = True)
    description=models.TextField()
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    credit = models.IntegerField()
    provider = models.TextField()
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField('Service Name', max_length=120)
    date = models.DateField('Service Date', blank=True, null = True)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    description=models.TextField()
    number_of_attendees = models.IntegerField()
    provider = models.TextField()
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name

# Create your models here.
