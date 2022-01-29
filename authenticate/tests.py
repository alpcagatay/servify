from venv import create
from django.test import TestCase, Client, TransactionTestCase, SimpleTestCase
from django.urls import reverse, resolve
from authenticate.models import User, Service, Event, Feed, Comment
from atexit import register
from django.shortcuts import resolve_url
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from authenticate.views import home, list_services,login_user, logout_user, register_user, edit_profile ,change_password, all_services, all_events, update_event, update_service, delete_event, delete_service, add_event, my_events, my_services, show_event, list_events, search_results,search_result_events, add_service, show_service, show_event, apply_service, apply_event, cancel_service, cancel_event, confirm_applied, confirm_applied_event, ShowProfilePageView, follow_user, unfollow_user, feed        
from django.test import SimpleTestCase
from authenticate.forms import SignUpForm, EditProfileForm, ServiceForm, EventForm, CommentForm



class TestViews(TestCase):

    
    def test_register(self):
        test_user = User.objects.create(
            username='UserTest',
            email = 'test@test.com',
            first_name = 'TestName',
            last_name = 'LastName',
            bio = 'Test Bio',
            password = 'Pass1919' ,
            profile_picture = 'media\download.png'
        )
        test_user.save()

        self.assertEqual(test_user.credit ,5)

    def test_add_service(self):
        test_user = User.objects.create(
            username='UserTest',
            email = 'test@test.com',
            first_name = 'TestName',
            last_name = 'LastName',
            bio = 'Test Bio',
            password = 'Pass1919' ,
            profile_picture = 'media\download.png'
        )
        test_user.save()

        test_service = Service.objects.create(
            name = 'TEST SERVICE',
            date = '2022-05-05',
            time = '19:00',
            description = 'TEST Description',
            credit = 1,
            service_picture = 'media\download.png',
            provider = test_user,
            cityname = 'Ankara',
            location = '39.933364,32.859742'

        )
        test_service.save()

        self.assertTrue(Service.objects.exists(),True)
        self.assertEqual(Service.objects.get(provider=test_user).name, 'TEST SERVICE')
        self.assertEqual(Service.objects.get(provider=test_user).cityname, 'Ankara')



    def test_add_event(self):
        test_user = User.objects.create(
            username='UserTest',
            email = 'test@test.com',
            first_name = 'TestName',
            last_name = 'LastName',
            bio = 'Test Bio',
            password = 'Pass1919' ,
            profile_picture = 'media\download.png'
        )
        test_user.save()

        test_service = Event.objects.create(
            name = 'TEST SERVICE',
            date = '2022-05-05',
            time = '19:00',
            description = 'TEST Description',
            credit = 1,
            service_picture = 'media\download.png',
            provider = test_user,
            cityname = 'Ankara',
            location = '39.933364,32.859742'

        )
        test_service.save()

        self.assertTrue(Event.objects.exists(),True)
        self.assertEqual(Event.objects.get(provider=test_user).description, 'TEST Description')
        self.assertEqual(Event.objects.get(provider=test_user).credit, 1)

class TestUrls (SimpleTestCase):

    def test_register_url(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_user)
    
    def test_login_url(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_user)

    def test_logout_url(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_user)

    def test_edit_profile_url(self):
        url = reverse('edit_profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_profile)

    def test_change_password_url(self):
        url = reverse('change_password')
        print(resolve(url))
        self.assertEquals(resolve(url).func, change_password)

    def test_all_services_url(self):
        url = reverse('all_services')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_services)

    def test_all_events_url(self):
        url = reverse('all_events')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_events)

    def test_add_event_url(self):
        url = reverse('add_event')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_event)

    def test_list_events_url(self):
        url = reverse('list_events')
        print(resolve(url))
        self.assertEquals(resolve(url).func, list_events)

    def test_add_service_url(self):
        url = reverse('add_service')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_service)

    def test_list_services_url(self):
        url = reverse('list_services')
        print(resolve(url))
        self.assertEquals(resolve(url).func, list_services)

    def test_search_results_url(self):
        url = reverse('search_results')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search_results)

    def test_search_results_events_url(self):
        url = reverse('search_results_events')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search_result_events)

    def test_my_events_url(self):
        url = reverse('my_events')
        print(resolve(url))
        self.assertEquals(resolve(url).func, my_events)

    def test_my_services_url(self):
        url = reverse('my_services')
        print(resolve(url))
        self.assertEquals(resolve(url).func, my_services)

    def test_feed_url(self):
        url = reverse('feed')
        print(resolve(url))
        self.assertEquals(resolve(url).func, feed)

class TestForms(SimpleTestCase):

    def test_signup_nodata_form(self):
        form = SignUpForm(data = {})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),8)

    def test_comment_form(self):
        form = CommentForm(data = {})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)

    def test_comment_form(self):
        form = CommentForm(data = {
            'body':'Example Comment'
        })
        self.assertTrue(form.is_valid())
