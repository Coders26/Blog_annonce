from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_authentication_success(self):
        url = reverse('authentification')
        data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('index'))

    def test_authentication_empty_fields(self):
        url = reverse('authentification')
        data = {
            'username': '',
            'password': ''
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('authentification'))

    def test_authentication_invalid_credentials(self):
        url = reverse('authentification')
        data = {
            'username': 'wronguser',
            'password': 'wrongpassword'
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('authentification'))

    def test_authentication_GET_request(self):
        url = reverse('authentification')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class SignupTestCase(TestCase):
    def test_signup_success(self):
        url = reverse('signup')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('authentification'))
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_signup_missing_fields(self):
        url = reverse('signup')
        data = {
            'username': '',
            'password': '',
            'confirm_password': ''
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_signup_password_mismatch(self):
        url = reverse('signup')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'confirm_password': 'mismatchedpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)


    def test_signup_GET_request(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)