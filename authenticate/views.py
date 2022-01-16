from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import EditProfileForm, EventForm, ServiceForm, SignUpForm
from urllib.parse import urlencode
from urllib.parse import urlparse, parse_qsl
from .models import Event, Service
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User = get_user_model()

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

@login_required
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

@login_required
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

@login_required
def event_detail(request):
    return render(request, 'event_detail.html')

@login_required
def service_detail(request):
    return render(request, 'service_detail.html')

@login_required
def search_result_events(request):
    return render(request, 'search_result_events.html')

@login_required
def search_result_services(request):
    return render(request, 'search_result_services.html')

@login_required
def user_profile(request):
    return render(request, 'user_profile.html')

@login_required
def service_creation(request):
    return render(request, 'service_creation.html')

@login_required
def event_creation(request):
    return render(request, 'event_creation.html')



@login_required
def all_services(request):
    service_list = Service.objects.all()
    return render(request, 'list_services.html', {'service_list': service_list })

@login_required
def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'list_events.html', {'event_list': event_list })

# def list_venues(request):
#     venue_list = Venue.objects.all()
#     return render(request, 'list_venues.html', {'venue_list': venue_list })

# def show_venue(request, venue_id):
#     venue = Venue.objects.get(pk = venue_id)
#     return render(request, 'show_venue.html', {'venue': venue })




# def add_venue(request):
#     submitted = False
#     if request.method == "POST":
#         form = VenueForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/add_venue?submitted=True')
#     else: 
#         form = VenueForm
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'add_venue.html', {'form':form, 'submitted':submitted})

@login_required
def update_event(request,event_id):
    event = Event.objects.get(pk = event_id)
    form = EventForm(request.POST or None,request.FILES,instance = event)
    if form.is_valid():
        form.save()
        return redirect('list_events')
    return render(request, 'update_event.html', {'event':event, 'form': form})

@login_required
def update_service(request,service_id):
    service = Service.objects.get(pk = service_id)
    form = ServiceForm(request.POST or None,request.FILES, instance = service)
    if form.is_valid():
        form.save()
        return redirect('list_services')
    return render(request, 'update_service.html', {'service':service, 'form': form})

@login_required
def delete_event(request, event_id):
    event = Event.objects.get(pk = event_id)
    event.delete()
    messages.success(request,("Event deleted!"))
    return HttpResponseRedirect('/list_events')
    
@login_required
def delete_service(request, service_id):
    service = Service.objects.get(pk = service_id)
    service.delete()
    messages.success(request,("Service deleted!"))
    return HttpResponseRedirect('/list_services')



@login_required
def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.provider = request.user
            event.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else: 
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_event.html', {'form':form, 'submitted':submitted})

@login_required
def my_events(request):
    if request.user.is_authenticated:
        events = Event.objects.filter(provider = request.user)
        return render(request, 'my_events.html', {'events':events})
    else:
        messages.success(request, ("You are not logged in"))
        return redirect('login')

def my_services(request):
    if request.user.is_authenticated:
        services = Service.objects.filter(provider = request.user)
        return render(request, 'my_services.html', {'services':services})
    else:
        messages.success(request, ("You are not logged in"))
        return redirect('login')




@login_required
def show_event(request, event_id):
    event = Event.objects.get(pk = event_id)
    return render(request, 'show_event.html', {'event': event, 'event_provider': event.provider })

@login_required
def list_events(request):
    event_list = Event.objects.all()
    return render(request, 'list_events.html', {'event_list': event_list })

@login_required
def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        result = Service.objects.filter(Q(description__contains=searched)| Q(name__contains=searched) | Q(venue__contains=searched) )
        return render(request, 'search_results.html', {'searched':searched, 'result':result })
    else:
        return render(request, 'search_results.html', {})

@login_required
def search_result_events(request):
    if request.method == "POST":
        looked = request.POST['looked']
        outcome = Event.objects.filter(Q(description__contains=looked)| Q(name__contains=looked) | Q(venue__contains=looked) )
        return render(request, 'search_result_events.html', {'looked':looked, 'outcome':outcome })
    else:
        return render(request, 'search_result_events.html', {})



@login_required
def add_service(request):
    submitted = False
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.provider = request.user
            service.save()
            return HttpResponseRedirect('/add_service?submitted=True')
    else: 
        form = ServiceForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_service.html', {'form':form, 'submitted':submitted})

@login_required
def show_service(request, service_id):
    user = request.user
    service = Service.objects.get(pk = service_id)
    is_user_applied = Service.objects.filter(pk = service_id, applied_ones=user).exists()
    can_user_apply = user.credit >= service.credit
    assigned_user =  service.attendees.first()
    return render(request, 'show_service.html', {
        'service': service, 
        "is_user_applied": is_user_applied, 
        "can_user_apply": can_user_apply, 
        "assigned_user": assigned_user 
    })

@login_required
def show_service2(request, service_id2):
    service2 = Service.objects.get(pk = service_id2)
    return render(request, 'show_service2.html', {'service2': service2 })


@login_required
def show_service_search(request, service_id):
    service = Service.objects.get(pk = service_id)
    return render(request, 'show_service.html', {'service': service })


@login_required
def list_services(request):
    service_list = Service.objects.all()
    return render(request, 'list_services.html', {'service_list': service_list })

@login_required
def apply_service(request, service_id):
    user = request.user
    service = Service.objects.get(pk = service_id)
    service.applied_ones.add(user)
    service.save()
    user.credit = user.credit - service.credit
    user.onholdcredit = user.onholdcredit + service.credit
    user.save()
    messages.success(request, ("Successfully applied"))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cancel_service(request, service_id):
    user = request.user
    service = Service.objects.get(pk = service_id)
    service.applied_ones.remove(request.user)
    service.save()
    user.credit = user.credit + service.credit
    user.onholdcredit = user.onholdcredit - service.credit
    user.save()
    messages.success(request, ("Successfully cancelled"))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
 

@login_required
def confirm_applied(request, service_id, user_id):
    applied_user = User.objects.get(id=user_id)
    service = Service.objects.get(pk = service_id)
    service.applied_ones.remove(applied_user)
    service.attendees.add(applied_user)
    service.provider.credit = service.provider.credit + service.credit
    service.provider.save()

    applied_user.onholdcredit = applied_user.onholdcredit - service.credit
    applied_user.save()

    for other_user in service.applied_ones.all():
        service.others.add(other_user)
        other_user.credit = other_user.credit + service.credit
        other_user.onholdcredit = other_user.onholdcredit - service.credit
        other_user.save()

    service.save()
    messages.success(request, ("Successfully applied"))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





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


