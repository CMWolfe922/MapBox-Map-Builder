from django.contrib import admin
from django.urls import path
from .views import AddressCreateView


urlpatterns = [
    path('', AddressCreateView.as_view(), name='home'),
]
