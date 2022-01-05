from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('change_password/', views.change_password, name="change_password"),

    path('event_detail/', views.event_detail, name="event_detail"),
    path('service_detail/', views.service_detail, name="service_detail"),
    path('search_result_events/', views.search_result_events, name="search_result_events"),
    path('search_result_services/', views.search_result_services, name="search_result_services"),
    path('user_profile/', views.user_profile, name="user_profile"),    
    path('service_creation/', views.service_creation, name="service_creation"),
    path('event_creation/', views.event_creation, name="event_creation"),

]
