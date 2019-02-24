from django.urls import path
from django.contrib.auth import views as auth_view
from blog import views

app_name = 'acccount'

urlpatterns = [
    # login url
    path('login/', auth_view.LoginView.as_view(template_name='account/registration/login.html'),
         name='login'),

    # logout url
    path('logout/', auth_view.LogoutView.as_view(template_name='account/registration/logged_out.html'),
         name='logout'),
    path('', views.post_list, name='post_list'),

    # change password urls
    path('password_change/', auth_view.PasswordChangeView.as_view(
        template_name='account/registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_view.PasswordChangeDoneView.as_view(
        template_name='account/registration/password_change_done.html'), name='password_change_done'),

    # reset password urls
    path('password_reset/', auth_view.PasswordResetView.as_view(
        template_name='account/registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='account/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='account/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(
        template_name='account/registration/password_reset_complete.html'), name='password_reset_complete'),
]
