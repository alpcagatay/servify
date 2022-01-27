from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User 
from django import forms
from django.db.models.base import Model
from django.forms import fields, ModelForm, widgets
from .models import Service, Event, Final_Event_Status, Final_Service_Status, Comment


from django.contrib.auth import get_user_model
User = get_user_model()

class EditProfileForm(UserChangeForm):
    password = forms.CharField(label = "" ,widget = forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password', "bio")


class SignUpForm(UserCreationForm):
    username = forms.CharField(label = "" ,max_length=150, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    email = forms.EmailField(label = "" ,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(help_text = "Enter Your First Name Here", label = "" ,max_length=100, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label = "" ,max_length=100,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    bio = forms.CharField(label = "" ,max_length=1000,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'bio'}))

    profile_picture = forms.ImageField()

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2','bio','profile_picture')

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

        self.fields['profile_picture'].widget.attrs['class']= ''
        self.fields['profile_picture'].widget.attrs['placeholder']= ''
        self.fields['profile_picture'].label = ''
        self.fields['profile_picture'].help_text = ''

        self.fields['bio'].widget.attrs['class']= 'form-control'
        self.fields['bio'].widget.attrs['placeholder']= 'bio'
        self.fields['bio'].label = ''
        self.fields['bio'].help_text = 'Please tell us about yourself.'




class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields =  ('name','date','time','description','venue','credit', 'service_picture')
        labels = {
            'name':'',
            'date':'',
            'time':'',
            'description':'',
            'venue':'',
            'credit':'',
            'service_picture':''
        }
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Service Name'}),
            'date': forms.TextInput(attrs={'type':'date','class':'form-control','placeholder':''}),
            'time': forms.TimeInput(attrs={'type':'time'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'venue': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue'}),
            'credit':forms.TextInput(attrs={'placeholder': 'Total Credit'}),
              }


    

class EventForm(ModelForm):
    class Meta:

        model = Event
        fields =  ('name','date','time','description','venue','event_picture','capacity')
        labels = {
            'name':'',
            'date':'',
            'time':'',
            'description':'',
            'venue':'',
            'credit':'',
            'event_picture':'',
            'capacity':'Capacity'
        }
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
            'date': forms.TextInput(attrs={'type':'date','class':'form-control','placeholder':''}),
            'time': forms.TimeInput(attrs={'type':'time'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'venue': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue'}),
       }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =  ('body',)
        labels = {
            'body':'',
        }
        widgets= {
            'body': forms.TextInput(attrs={'class':'form-control','placeholder':'Comment'}),
        }  