from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',
    	views.register,
    		name='userprofiles-register')
    ,
    path('profile/',
    	views.profile,
    		name='userprofiles-profile')
    ,
    path('login/',
    	auth_views.LoginView.as_view(
    		template_name='userprofiles/login.html'),
    		name='userprofiles-login')
    ,
    path('logout/',
    	auth_views.LogoutView.as_view(
    		template_name='userprofiles/logout.html'),
    		name='userprofiles-logout')
    ,
    path('password-reset/',
    	auth_views.PasswordResetView.as_view(
    		template_name='userprofiles/password_reset.html'), 
    		name='userprofiles-password_reset')
    ,
    path('password-reset/done/',
    	auth_views.PasswordResetDoneView.as_view(
    		template_name='userprofiles/password_reset_done.html'), 
    		name='password_reset_done')
    ,
    path('password-reset/confirm/<uidb64>/<token>/',
    	auth_views.PasswordResetConfirmView.as_view(
    		template_name='userprofiles/password_reset_confirm.html'), 
    		name='password_reset_confirm')
    ,
    path('password-reset-complete',
    	auth_views.PasswordResetCompleteView.as_view(
    		template_name='userprofiles/password_reset_complete.html'), 
    		name='password_reset_complete')
    ,
]
