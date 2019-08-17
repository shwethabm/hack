from django.urls import path, include
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('password/', user_views.change_password, name='change_password'),
]