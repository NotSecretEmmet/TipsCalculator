from django.test import TestCase, Client
from django.urls import reverse
from tips.models import TipsRun, TipsResults
import json
import unittest

from django.contrib.auth.models import User

class TestViews(TestCase):
	
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user('johnlennon', 'lennon@thebeatles.com', 'johnpassword')

	def testLogin(self):
		self.client.login(
			username='johnlennon', 
			password='johnpassword'
		)
		response = self.client.get(reverse('userprofiles-login'))
		self.assertEqual(response.status_code, 200)

	def test_calculator_view_GET(self):
		self.client.force_login(self.user)
		response = self.client.get(reverse('tips-calculator'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'tips/calculator.html')

	def test_history_view_GET(self):
		self.client.force_login(self.user)
		response = self.client.get(reverse('tips-history'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'tips/history.html')