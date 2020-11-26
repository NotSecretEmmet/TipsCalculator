from django.test import TestCase, Client
from tips.forms import UploadFileForm
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.conf import settings
from django.contrib.auth.models import User
from tips import tips_utils

class TestForms(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user('johnlennon', 'lennon@thebeatles.com', 'johnpassword')


		self.file_path_eng = os.path.join(settings.MEDIA_ROOT, 'test_file_eng.xls')
		self.file_path_nl = os.path.join(settings.MEDIA_ROOT, 'test_file_nl.xlsx')
		self.file_path_blank = os.path.join(settings.MEDIA_ROOT, 'test_file_blank.xlsx')
		self.data = {
			'check_isoweek' : False,
			'tips_amount' : 1000,
			'overtips_amount' : 50,
		}
		with open(self.file_path_eng, 'rb') as f:
			self.form_eng = UploadFileForm(
				data=self.data, 
				files={'Dyflexis_excel_export' : SimpleUploadedFile('Dyflexis_excel_export', f.read())}
			)

	def test_upload_form_invalid_data(self):
		form = UploadFileForm()
		self.assertFalse(form.is_valid())

	def test_upload_form_valid_data(self):
		self.assertTrue(self.form_eng.is_valid())

	def test_form_response(self):
		self.client.login(
			username='johnlennon', 
			password='johnpassword'
		)
		self.response = self.client.post(reverse('tips-calculator'), form=self.form_eng)
		self.assertRedirects(self.response, '/calculator/')

	def test_tips_check_input_blank(self):
		with open(self.file_path_blank, 'rb') as f:
			error_boo, msg = tips_utils.check_input(
				SimpleUploadedFile('Dyflexis_excel_export', f.read()),
				self.data['check_isoweek'],
				self.data['tips_amount'],
				self.data['overtips_amount']
			)
		self.assertTrue(error_boo)

	def test_tips_check_input_eng(self):
		with open(self.file_path_eng, 'rb') as f:
			error_boo, msg = tips_utils.check_input(
				SimpleUploadedFile('Dyflexis_excel_export', f.read()),
				self.data['check_isoweek'],
				self.data['tips_amount'],
				self.data['overtips_amount']
			)
		self.assertFalse(error_boo)

	def test_tips_check_input_nl(self):
		with open(self.file_path_nl, 'rb') as f:
			error_boo, msg = tips_utils.check_input(
				SimpleUploadedFile('Dyflexis_excel_export', f.read()),
				self.data['check_isoweek'],
				self.data['tips_amount'],
				self.data['overtips_amount']
			)
		self.assertFalse(error_boo)

	def test_tips_check_input_isoweek_invalid(self):
		with open(self.file_path_eng, 'rb') as f:
			error_boo, msg = tips_utils.check_input(
				SimpleUploadedFile('Dyflexis_excel_export', f.read()),
				True,
				self.data['tips_amount'],
				self.data['overtips_amount']
			)
		self.assertTrue(error_boo)		

	def test_tips_check_input_isoweek_valid(self):
		with open(self.file_path_nl, 'rb') as f:
			error_boo, msg = tips_utils.check_input(
				SimpleUploadedFile('Dyflexis_excel_export', f.read()),
				True,
				self.data['tips_amount'],
				self.data['overtips_amount']
			)
		self.assertFalse(error_boo)	

	def test_tips_processing_eng(self):
		with open(self.file_path_eng, 'rb') as f:
			tipsrun_entry = tips_utils.process_tips(
				SimpleUploadedFile('Dyflexis_excel_export', f.read()), 
				self.data['tips_amount'], 
				self.data['overtips_amount'], 
				self.user
			)
		self.assertEqual(tipsrun_entry.user, self.user)

	def test_tips_processing_nl(self):
		with open(self.file_path_nl, 'rb') as f:
			tipsrun_entry = tips_utils.process_tips(
				SimpleUploadedFile('Dyflexis_excel_export', f.read()), 
				self.data['tips_amount'], 
				self.data['overtips_amount'], 
				self.user
			)
		self.assertEqual(tipsrun_entry.user, self.user)

