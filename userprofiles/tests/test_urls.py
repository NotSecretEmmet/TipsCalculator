from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from userprofiles.views import register, profile


class TestUrls(SimpleTestCase):

	def test_register_url_is_resolved(self):
		url = reverse('userprofiles-register')
		self.assertEquals(resolve(url).func, register)

	def test_login_url_is_resolved(self):
		url = reverse('userprofiles-login')
		self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

	def test_logout_url_is_resolved(self):
		url = reverse('userprofiles-logout')
		self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)

	def test_profile_url_is_resolved(self):
		url = reverse('userprofiles-profile')
		self.assertEquals(resolve(url).func, profile)

	def test_password_reset_url_is_resolved(self):
		url = reverse('userprofiles-password_reset')
		self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetView)