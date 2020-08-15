from django.urls import path

urlpatterns = [
    path('', view.home, name='home'),
]
