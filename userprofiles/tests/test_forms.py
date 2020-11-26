from django.test import TestCase, Client
from userprofiles.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.contrib.auth.models import User


class TestForms(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user('johnlennon', 'lennon@thebeatles.com', 'johnpassword')


	def test_profile_update_form_invalid_data(self):
		p_form = ProfileUpdateForm()
		self.assertFalse(p_form.is_valid())

	def test_profile_update_form_valid_data(self):
		data = {
			'user' : self.user,
			'image' : None,
			'active' : True,
			'locatie' : 'CS',

		}
		self.p_form = ProfileUpdateForm(data=data)
		self.assertTrue(self.p_form.is_valid())


	def test_user_update_form_invalid_data(self):
		u_form = UserUpdateForm()
		self.assertFalse(u_form.is_valid())
