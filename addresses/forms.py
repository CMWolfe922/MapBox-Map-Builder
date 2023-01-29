from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Address
from django.contrib.auth.models import User

class AddressInputForm(ModelForm):
    model = Address

    class Meta:
        fields =['name', 'address']


class UserLoginForm(UserCreationForm):
    model = User

    class Meta:
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
