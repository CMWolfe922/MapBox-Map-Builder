from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView
from .models import Address
from .forms import AddressInputForm


class AddressCreateView(CreateView):

    model = Address
    fields = ['address']
    context_object_name = 'addresses'
    template_name = 'addresses/home.html'
    success_url = '/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = Address.objects.all()
        context['mapBoxAccessToken'] = 'pk.eyJ1IjoiY213b2xmZSIsImEiOiJjbGQxMnFjbTExdWt0M3Z0N2hzZThqZ3luIn0.ZvKlTXVuzS9MZegMWAhGPw'
        return context


class BaseMapIndexView(TemplateView):

    model = Address
    template_name = 'index.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = Address.objects.all()
        context['mapBoxAccessToken'] = 'pk.eyJ1IjoiY213b2xmZSIsImEiOiJjbGQxMnFjbTExdWt0M3Z0N2hzZThqZ3luIn0.ZvKlTXVuzS9MZegMWAhGPw'
        return context
