from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views as blog_views
from . import views as account_views

app_name = 'account'

urlpatterns = [
    # login url
    path('login/', auth_views.LoginView.as_view(), name='login'),

    # logout url
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', blog_views.post_list, name='post_list'),

    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url='done/'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url='complete/'),
         name='password_reset_confirm'),

    path('reset/<uidb64>/<token>/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('register/', account_views.register, name='register'),

    path('edit/', account_views.edit, name='edit'),
]
