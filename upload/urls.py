from django.urls import path, include
from . import views


urlpatterns = [
    path('upload/', views.upload, name='upload'),

]