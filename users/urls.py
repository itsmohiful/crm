from django.urls import include, path

from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile, name='profile'),
    path('profile/update',views.update_profile, name='update_profile'),
]
