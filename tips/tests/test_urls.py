from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tips.views import CalculatorView, HistoryView, ResultsView


class TestUrls(SimpleTestCase):

	def test_tips_calculator_url_is_resolved(self):
		url = reverse('tips-calculator')
		self.assertEquals(resolve(url).func.view_class, CalculatorView)

	def test_tips_history_url_is_resolved(self):
		url = reverse('tips-history')
		self.assertEquals(resolve(url).func.view_class, HistoryView)

	def test_tips_results_url_is_resolved(self):
		url = reverse('tips-results', args=['1'])
		self.assertEquals(resolve(url).func.view_class, ResultsView)
		