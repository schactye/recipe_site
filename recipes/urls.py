from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('breakfast/', views.breakfast_list, name='breakfast'),
    path('lunch/', views.lunch_list, name='lunch'),
    path('dinner/', views.dinner_list, name='dinner'),
]