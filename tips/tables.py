import django_tables2 as tables
from .models import TipsRun, TipsResults

class TipsResultsTable(tables.Table):
	class Meta:
		model = TipsResults
		template_name = 'django_tables2/bootstrap4.html'
		fields = (
			'personeelsnummer',
			'naam', 
			'boh_hours', 
			'foh_hours', 
			'total_hours', 
			'boh_tips', 
			'foh_tips', 
			'total_tips'
		)
		row_attrs={
            'style' : "height:10px"
        }

class TipsRunTable(tables.Table):
	class Meta:
		model = TipsRun
		template_name = 'django_tables2/semantic.html'
		fields = (
			'boh_hours', 
			'boh_tipr', 
			'foh_hours', 
			'foh_tipr', 
			'tips_amount', 
			'overtips_amounts', 
			'effective_tips'
		)

 