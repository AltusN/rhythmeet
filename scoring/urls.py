from django.urls import path

from . import views

urlpatterns = [
    path('gymnast/', views.view_all_gymnasts, name='Gymnasts'),
]