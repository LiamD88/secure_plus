from django.urls import path
from . import views

urlpatterns = [
    path('', views.services1, name='services1'),
    path('oneoff', views.oneoff, name='oneoff'),
    path('yearly', views.yearly, name='yearly'),
    path('monthly', views.monthly, name='monthly')
]
