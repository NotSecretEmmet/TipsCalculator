from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
	template_name = 'main/home.html'
	login_url = reverse_lazy('userprofiles-login')

class FaqView(LoginRequiredMixin, TemplateView):
	template_name = 'main/faq.html'
	login_url = reverse_lazy('userprofiles-login')