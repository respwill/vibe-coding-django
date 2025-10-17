from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserAuthTests(TestCase):
	def test_register(self):
		response = self.client.post(reverse('register'), {
			'username': 'testuser',
			'password1': 'testpass1234',
			'password2': 'testpass1234',
		})
		self.assertEqual(response.status_code, 302)
		self.assertTrue(User.objects.filter(username='testuser').exists())

	def test_login(self):
		User.objects.create_user(username='testuser', password='testpass1234')
		response = self.client.post(reverse('login'), {
			'username': 'testuser',
			'password': 'testpass1234',
		})
		self.assertEqual(response.status_code, 302)
		self.assertTrue('_auth_user_id' in self.client.session)
