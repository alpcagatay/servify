from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from django import forms
from django.db.models.base import Model
from django.forms import fields, ModelForm, widgets
from .models import MyClubUser, Service, Event, Final_Event_Status, Final_Service_Status

class EditProfileForm(UserChangeForm):
    password = forms.CharField(label = "" ,widget = forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password',)


class SignUpForm(UserCreationForm):
    username = forms.CharField(label = "" ,max_length=100,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(label = "" ,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(help_text = "Enter Your First Name Here", label = "" ,max_length=100, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label = "" ,max_length=100,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['username'].widget.attrs['placeholder']= 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'




        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['placeholder']= 'Password'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['placeholder']= 'Confirm Password'
        self.fields['password2'].label = ''


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields =  ('name','date','time','description','venue','attendees','credit','provider','service_picture')
        
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Service Name'}),
            'date': forms.TextInput(attrs={'type':'date','class':'form-control','placeholder':''}),
            'time': forms.TimeInput(attrs={'type':'time'}),
            'description': forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
            'venue': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue'}),
            'attendees': forms.TextInput(attrs={'class':'form-control','placeholder':'Attendees'}),
            'credit':forms.TextInput(attrs={'placeholder': 'Total Credit'}),
            'provider':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Provider'})
       }


    

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields =  ('name','date','time','description','venue','attendees','service_picture')
        
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
            'date': forms.TextInput(attrs={'type':'date','class':'form-control','placeholder':''}),
            'time': forms.TimeInput(attrs={'type':'time'}),
            'description': forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
            'venue': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue'}),
            'attendees': forms.TextInput(attrs={'class':'form-control','placeholder':'Attendees'}),
       }