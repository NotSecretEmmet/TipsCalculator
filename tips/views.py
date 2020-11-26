from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_tables2 import RequestConfig, MultiTableMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView

from userprofiles.models import Profile
from .models import TipsRun, TipsResults
from .forms import UploadFileForm
from .tables import TipsResultsTable, TipsRunTable
from . import tips_utils

class CalculatorView(LoginRequiredMixin, TemplateView):
	template_name = 'tips/calculator.html'
	login_url = reverse_lazy('userprofiles-login')

	def get(self, request, *args, **kwargs):
		form = UploadFileForm()
		return render(request, 'tips/calculator.html', {'form': form})

	def post(self, request, *args, **kwargs):
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			tips_amount = form.cleaned_data.get('tips_amount')
			overtips_amount = form.cleaned_data.get('overtips_amount')
			check_week = form.cleaned_data.get('check_isoweek')
			tips_file = request.FILES['Dyflexis_excel_export'] 
			error_boo, msg = tips_utils.check_input(tips_file, check_week, tips_amount, overtips_amount)
			if error_boo:
				messages.warning(request, msg)
				return redirect('tips-calculator')
			else:
				tipsrun_entry = tips_utils.process_tips(tips_file, tips_amount, overtips_amount, request.user)
				if tipsrun_entry:
						return redirect(f'/calculator/results/{tipsrun_entry.id}/')
		else:
			messages.warning(request, 'Unknown error')
			return redirect('tips-calculator')


class ResultsView(LoginRequiredMixin, DetailView):
	model = TipsRun
	template_name = 'tips/results.html'

	def get_context_data(self, **kwargs):
		context = super(ResultsView, self).get_context_data(**kwargs)
		run_table = TipsRunTable(TipsRun.objects.filter(pk=kwargs['object'].pk).all())
		RequestConfig(self.request).configure(run_table)
		context['run_table'] = run_table
		tipsrun_i = TipsRun.objects.filter(pk=kwargs['object'].pk).first()
		results_table = TipsResultsTable(TipsResults.objects.filter(tipsrun= tipsrun_i).all())
		RequestConfig(self.request, paginate={'per_page' : 100}).configure(results_table)
		context['results_table'] = results_table
		return context

	def post(self, request, *args, **kwargs):
		tipsrun_i = TipsRun.objects.filter(pk=kwargs['pk']).first()
		export_fn = tipsrun_i.locatie + tipsrun_i.week
		response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',)
		response['Content-Disposition'] = f'attachment; filename={tipsrun_i.locatie + tipsrun_i.week}.xlsx'
		workbook = tips_utils.export_run_to_excel(tipsrun_i)
		workbook.save(response)
		return response
	

class HistoryView(LoginRequiredMixin, ListView):
	template_name = 'tips/history.html'
	login_url = reverse_lazy('userprofiles-login')
	model = TipsRun

	def get_queryset(self):
		return TipsRun.objects.filter(locatie=self.request.user.profile.locatie).order_by('run_dt').reverse().all()
