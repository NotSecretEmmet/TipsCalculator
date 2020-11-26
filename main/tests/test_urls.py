from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import HomeView, FaqView


class TestUrls(SimpleTestCase):

	def test_main_home_url_is_resolved(self):
		url = reverse('main-home')
		self.assertEquals(resolve(url).func.view_class, HomeView)

	def test_main_faq_url_is_resolved(self):
		url = reverse('main-faq')
		self.assertEquals(resolve(url).func.view_class, FaqView)