from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('change_password/', views.change_password, name="change_password"),
    path('all_services/', views.all_services, name="all_services"),
    path('all_events/', views.all_events, name="all_events"),
    path('event_detail/', views.event_detail, name="event_detail"),
    path('service_detail/', views.service_detail, name="service_detail"),
    path('user_profile/', views.user_profile, name="user_profile"),    
    path('service_creation/', views.service_creation, name="service_creation"),
    path('event_creation/', views.event_creation, name="event_creation"),
    path('mapindex/', views.mapindex, name="mapindex"),
    path('add_event/', views.add_event, name="add_event"),
    path('list_events/', views.list_events, name="list_events"),
    path('show_event/<event_id>', views.show_event, name="show_event"),
    path('add_service/', views.add_service, name="add_service"),
    path('list_services/', views.list_services, name="list_services"),
    path('show_service/<service_id>', views.show_service, name="show_service"),
    path('search_results', views.search_results, name="search_results"),
    path('search_result_events', views.search_result_events, name="search_results_events"),
    path('show_service2/<service_id>', views.show_service2, name="show_service2"),


]
