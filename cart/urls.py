from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<id>/', views.add_to_cart, name='add_to_cart'),
    path('amend/<id>/', views.amend_cart, name='amend_cart'),
]
