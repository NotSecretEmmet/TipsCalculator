from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from tips.models import TipsRun, TipsResults
import pytz

class TestModels(TestCase):

	def setUp(self):
		self.user = User.objects.create_user('johnlennon', 'lennon@thebeatles.com', 'johnpassword')

		self.tipsrun1 = TipsRun.objects.create(
			start_dt = timezone.now(),
			end_dt = timezone.now(),
			run_dt = timezone.now(),
			boh_hours = 100,
			boh_tipr = 0.15,
			foh_hours = 100,
			foh_tipr = 0.15,
			tips_amount = 1000,
			overtips_amounts = 50,
			effective_tips = 950,
			locatie = 'CS',
			week = '2020W1',
			user = self.user
		)

		self.tipsresult1 = TipsResults.objects.create(
			personeelsnummer = '1000',
			naam = 'TestName',
			boh_hours = 10,
			foh_hours = 10,
			total_hours = 20,
			boh_tips = 10,
			foh_tips = 10,
			total_tips = 20,
			tipsrun = self.tipsrun1,
			user = self.user,
		)

	def test_tipsrun(self):
		self.assertTrue(self.tipsrun1.tips_amount, 1000)

	def test_tipsresult(self):
		self.assertTrue(self.tipsresult1.total_tips, 20)
	
	def test_results_view_GET(self):
		self.client.force_login(self.user)
		test_pk = self.tipsrun1.pk
		response = self.client.get(reverse('tips-results', args=[test_pk]))

		# self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'tips/results.html')