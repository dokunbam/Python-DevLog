
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path('password_change', auth_views.PasswordResetView.as_view(
        template_name='passreset/password_reset_form.html',  
        email_template_name='passreset/password_reset_email.html', 
        subject_template_name='passreset/password_reset_subject.txt'), name='password_change'),
    
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='passreset/password_reset_done.html'),name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='passreset/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('password_reset/complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='passreset/password_reset_complete.html'), name='password_reset_complete'),

    path('settings/password/', auth_views.PasswordChangeView.as_view(
        template_name='passreset/password_change.html'), name='auth_password_change'),

    path('settings/password/done', auth_views.PasswordChangeDoneView.as_view(
        template_name='passreset/passwordchangedone.html'), name='auth_password_change_done'),
    
    #path('accounts/password_reset/', name='password_reset'),
    
   
    

]

  #path('accounts/password_change/', name='password_change'),
   # path('accounts/password_change/done/', name='password_change_done'),
    #path('accounts/password_reset/', name='password_reset'),
    #path('accounts/password_reset/done/', name='password_reset_done'),
    #path('accounts/reset/<uidb64>/<token>/', name='password_reset_confirm'),
    #path('accounts/reset/done/', name='password_reset_complete')