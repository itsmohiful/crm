from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile, name='profile'),
    path('profile/update',views.update_profile, name='update_profile'),

    #password
    path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_sent/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
