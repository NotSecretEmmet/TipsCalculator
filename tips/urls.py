from django.urls import path
from .views import CalculatorView, HistoryView, ResultsView

urlpatterns = [
    path('',
    	CalculatorView.as_view(), 
     		name='tips-calculator')
    ,
    path('history/',
    	HistoryView.as_view(), 
     		name = 'tips-history')
    ,
    path('results/<int:pk>/',
    	ResultsView.as_view(), 
     		name='tips-results')
	]
