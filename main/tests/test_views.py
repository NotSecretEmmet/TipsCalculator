from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):
	
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user('johnlennon', 'lennon@thebeatles.com', 'johnpassword')

	def test_home_view_GET(self):
		self.client.force_login(self.user)
		response = self.client.get(reverse('main-home'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/home.html')

	def test_faq_view_GET(self):
		self.client.force_login(self.user)
		response = self.client.get(reverse('main-faq'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/faq.html')

