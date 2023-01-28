from django import forms
from django.forms import ModelForm
from .models import Address


class AddressInputForm(ModelForm):
    model = Address

    class Meta:
        fields =['address']

    def mark_address(self, address):
        """
        Create a marker on the map with the address.
        """
        pass
