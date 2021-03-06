from email.policy import default
from django import forms
from django.core import validators
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import related
from django.db.models.fields.related import ManyToManyField
from django.forms import IntegerField, widgets
from django.forms.models import ModelForm
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from location_field.models.plain import PlainLocationField



# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if email:
            email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name="Username",
        max_length=150,
        blank=False,
        null=False,
        unique=True,
    )
    email = models.EmailField(
        verbose_name="Email address",
        max_length=96,
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        verbose_name="First name",
        max_length=30,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name="Last name",
        max_length=30,
        blank=True,
        null=True,
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name="Date joined",
    )
    is_superuser = models.BooleanField(
        verbose_name="Super user",
        default=False,
    )
    is_staff = models.BooleanField(
        verbose_name="Staff",
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name="Active",
        default=True,
    )
    profile_picture = models.ImageField(
        verbose_name="Profile picture",
        null=True, 
        blank=True, 
        upload_to = "images/profile/",
    )
    bio = models.TextField(
        verbose_name="Bio",
        blank=True,
        null=True,
    )
    credit = models.PositiveBigIntegerField(
        verbose_name="Credit",
        default=5, 
        validators = [MaxValueValidator(15),MinValueValidator(0)],
    )
    onholdcredit = models.PositiveIntegerField(
        verbose_name="On hold credit",
        default=0, 
        validators = [MaxValueValidator(15), MinValueValidator(0)]
    )
    followers = models.ManyToManyField("authenticate.User", 
        blank=True, 
        related_name='followers_users'
        
    )
    numberoffollowers = models.PositiveBigIntegerField(
        verbose_name="numberoffollowers",
        default=0,
    )
   
    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return " ".join([self.first_name, self.last_name])


# class followers(models.Model):
#     followers = models.ManyToManyField("authenticate.User", blank=True, related_name='followers')
#     numberoffollowers = models.PositiveIntegerField(default = 0)

class Service(models.Model):
    name = models.CharField('Service Name', max_length=120)
    date = models.DateField('Service Date', blank=True, null = True)
    time = models.TimeField(default='12:00')
    description=models.TextField()
    credit = models.PositiveIntegerField()
    service_picture = models.ImageField(null=True, blank=True)
    provider = models.ForeignKey("authenticate.User", on_delete=models.CASCADE, related_name='service_provider')
    applied_ones = models.ManyToManyField("authenticate.User",default="", blank=True, related_name='service_applied_ones')
    attendees = models.ManyToManyField("authenticate.User",default="", blank=True, related_name='service_attendees')
    others = models.ManyToManyField("authenticate.User", default="", blank=True, related_name='service_others')
    service_picture = models.ImageField(null=True, blank=True, upload_to = "images/")
    cityname = models.CharField(max_length=255, default='Ankara')
    location = PlainLocationField(based_fields=['cityname'], zoom=8)

    ChoicesForService = ((1,'Open'),(2,'Closed'),(3,'Done'))
    status = models.PositiveIntegerField(choices=ChoicesForService, default = 1)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    date = models.DateField('Event Date', blank=True, null = True)
    time = models.TimeField(default='12:00')
    description=models.TextField()
    credit = models.PositiveIntegerField(default=0)
    service_picture = models.ImageField(null=True, blank=True)
    provider = models.ForeignKey("authenticate.User", on_delete=models.CASCADE, related_name='event_provider')
    applied_ones = models.ManyToManyField("authenticate.User",default="", related_name='event_applied_ones')
    attendees = models.ManyToManyField("authenticate.User",default="", blank=True, related_name='event_attendees')
    others = models.ManyToManyField("authenticate.User", default="", blank=True, related_name='event_others')
    event_picture = models.ImageField(null=True, blank=True, upload_to = "images/")
    capacity = models.PositiveIntegerField(default=10)
    cityname = models.CharField(max_length=255, default='Ankara')
    location = PlainLocationField(based_fields=['cityname'], zoom=8)
   
    ChoicesForService = ((1,'Open'),(2,'Closed'),(3,'Done'))
    status = models.PositiveIntegerField(choices=ChoicesForService, default = 1)

    def __str__(self):
        return self.name


class Final_Event_Status(models.Model):
    user_final_status = models.ManyToManyField(User, default="", related_name='event_user_status')
    event_final_status = models.ManyToManyField(Service, default="", related_name='event_final_status')
    choices = ((1,'Applied'), (2,'Accepted'),(3,'Completed'), (4,'Not Completed'),(5,'Rejected'))
    user_final_status = models.PositiveIntegerField(choices=choices)


# # Create your models here.

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


class Feed(models.Model):
    feed_user = models.ForeignKey("authenticate.User",default = "", null=True, blank=True, on_delete=models.CASCADE, related_name='feed_user')
    feed_user2 = models.ForeignKey("authenticate.User", default = "", null=True, blank=True,on_delete=models.CASCADE, related_name='feed_user2')
    feed_service = models.ForeignKey(Service, default = "", null=True, blank=True, on_delete=models.CASCADE, related_name='feed_service')
    feed_event = models.ForeignKey(Event, default = "", null=True, blank=True, on_delete=models.CASCADE, related_name='feed_event')
    feed_date = models.DateTimeField()
    choices = ((1, 'registered'),(2,'logged in'),(3,'followed'),(4,'unfollowed'), (5,'created an event'),(6,'created a service'),(7,'applied service'),(8,'applied event'),(9,'confirmed'), (10, 'updated event'),(11,'deleted an event'),(12,('edited profile information')), (13, 'updated service'), (14, 'deleted a service'), (15,'canceled application'), (16,('cancelled application to an event')),(17,('confirmed event')),(18,('commented on')),(18,('commented on event')))
    feed_status = models.PositiveIntegerField(choices=choices)

class Comment(models.Model):
    servicecom = models.ForeignKey(Service, default = "", null=True, blank=True, on_delete=models.CASCADE, related_name='scomments')
    eventcom = models.ForeignKey(Event, default = "", null=True, blank=True, on_delete=models.CASCADE, related_name='ecomments')
    usercomment = models.ForeignKey("authenticate.User",default = "", null=True, blank=True, on_delete=models.CASCADE, related_name='user_commented')
    body = models.TextField()
    datecomment = models.DateTimeField(auto_now_add=True)


class Place(models.Model):
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7, default = 'Ankara')


# class Place(models.Model):
#     parent_place = models.ForeignKey(
#         'self',
#         null=True,
#         blank=True,
#         on_delete=models.CASCADE,
#     )

#     city = models.CharField(max_length=255)
   