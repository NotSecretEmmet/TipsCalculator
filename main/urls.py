from django.urls import path
from .views import HomeView, FaqView

urlpatterns = [
    path('',
    	HomeView.as_view(),
     		name='main-home')
    ,
    path('faq/',
    	FaqView.as_view(),
    		name='main-faq')
	]
