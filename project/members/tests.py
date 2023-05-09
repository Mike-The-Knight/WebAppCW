from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Profile


class UserRegistrationTestCase(TestCase):

    def test_user_registration(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())


class UserAuthenticationTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )

    def test_user_signin(self):
        response = self.client.post(reverse('signin'), {
            'username': 'testuser',
            'password': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_user_signout(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('signout'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class UserProfileTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )

    def test_user_profile_created(self):
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_user_profile_view(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('view_user', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
