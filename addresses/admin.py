from django.contrib import admin
from .models import Address, Route, RouteTag, Driver, Delivery



admin.site.register(Route)
admin.site.register(Delivery)
admin.site.register(Address)
admin.site.register(Driver)
admin.site.register(RouteTag)
