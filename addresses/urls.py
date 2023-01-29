from django.contrib import admin
from django.urls import path
from .views import AddressCreateView, BaseMapIndexView


urlpatterns = [
    path('home/', AddressCreateView.as_view(), name='home'),
    path('', BaseMapIndexView.as_view(), name='index'),
]
