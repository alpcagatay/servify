from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import EditProfileForm, EventForm, ServiceForm, SignUpForm
from urllib.parse import urlencode
from urllib.parse import urlparse, parse_qsl
from .models import Event, MyClubUser, Service, Venue
from .forms import VenueForm
from django.http import HttpResponseRedirect
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request,'home.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('You have been logged in.'))
            return redirect('home')
        else:
            messages.success(request,('Ooops! Something went wrong. Please Try Again.'))
            return redirect('login')  
    else:
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,('You have been logged out!'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username = username, password=password)
            login(request,user)
            messages.success(request,('You have registered'))
            return redirect('home')

    else:
        form = SignUpForm()
    
    context = {'form':form}
    return render(request, 'register.html',context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
           
            messages.success(request,('You have edited your profile'))
            return redirect('home')

    else:
        form = EditProfileForm(instance=request.user)
    
    context = {'form':form}
    return render(request, 'edit_profile.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(date=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,('You have edited your password'))
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)
    
    context = {'form':form}
    return render(request, 'change_password.html',context)

def event_detail(request):
    return render(request, 'event_detail.html')

def service_detail(request):
    return render(request, 'service_detail.html')

def search_result_events(request):
    return render(request, 'search_result_events.html')

def search_result_services(request):
    return render(request, 'search_result_services.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def service_creation(request):
    return render(request, 'service_creation.html')

def event_creation(request):
    return render(request, 'event_creation.html')



def all_services(request):
    service_list = Service.objects.all()
    return render(request, 'all_services.html', {'service_list': service_list })

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'all_events.html', {'event_list': event_list })

def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'list_venues.html', {'venue_list': venue_list })

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk = venue_id)
    return render(request, 'show_venue.html', {'venue': venue })




def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else: 
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_venue.html', {'form':form, 'submitted':submitted})



def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else: 
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_event.html', {'form':form, 'submitted':submitted})

def show_event(request, event_id):
    event = Event.objects.get(pk = event_id)
    return render(request, 'show_event.html', {'event': event })

def list_events(request):
    event_list = Event.objects.all()
    return render(request, 'list_events.html', {'event_list': event_list })

def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        result = Service.objects.filter(description__contains=searched)
        return render(request, 'search_results.html', {'searched':searched, 'result':result })
    else:
        return render(request, 'search_results.html', {})

def search_results_events(request):
    if request.method == "POST":
        looked = request.POST['looked']
        outcome = Event.objects.filter(description__contains=looked)
        return render(request, 'search_results_events.html', {'looked':looked, 'outcome':outcome })
    else:
        return render(request, 'search_results_events.html', {})



def add_service(request):
    submitted = False
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_service?submitted=True')
    else: 
        form = ServiceForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_service.html', {'form':form, 'submitted':submitted})

def show_service(request, service_id):
    event = Service.objects.get(pk = service_id)
    return render(request, 'show_service.html', {'event': event })

def list_services(request):
    service_list = Service.objects.all()
    return render(request, 'list_services.html', {'service_list': service_list })


def mapindex(address_or_postalcode, data_type = 'json'):
    #def extract_lat_lang
    #Create Map Object
    api_key = "AIzaSyA6k5eadUusSfdDx5GzCXFW_HlBekTN_VU"
    data_type = 'json'
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_postalcode, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200,299):
        return {}    
    latlng = {}
    try: 
        return r.json(['results'])[0]['geometry']['location']
    except:
        pass
    return latlng.get("lat"), latlng.get("lng")

    parsed_url = urlparse(to_parse)
    query_string = parsed_url.query
    

    return render(url, 'mapindex.html')


