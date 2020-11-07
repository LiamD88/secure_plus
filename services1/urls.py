from django.urls import path
from . import views

urlpatterns = [
    path('', views.services1, name='services1')
]
