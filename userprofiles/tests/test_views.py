from django.test import TestCase, Client
from django.urls import reverse
from userprofiles.models import Profile
from userprofiles.views import register, profile
from django.contrib.auth.models import User

class TestViews(TestCase):
	
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user('johnlennon', 'lennon@thebeatles.com', 'johnpassword')

	def test_register_view_GET(self):
		response = self.client.get(reverse('userprofiles-register'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'userprofiles/register.html')

	def test_register_view_POST(self):
		pass

	def test_profile_view_GET(self):
		self.client.login(username='johnlennon', password='johnpassword')
		response = self.client.get(reverse('userprofiles-profile'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'userprofiles/profile.html')

	def test_profile_view_POST(self):
		pass

