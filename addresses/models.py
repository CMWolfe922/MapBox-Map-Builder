import geocoder
from django.db import models


# mapbox.com API key
MAPBOX_API_KEY = "pk.eyJ1IjoiY213b2xmZSIsImEiOiJjbGQxMnFjbTExdWt0M3Z0N2hzZThqZ3luIn0.ZvKlTXVuzS9MZegMWAhGPw"


class Route(models.Model):
    hub_location = models.CharField(max_length=3, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)


class RouteCode(models.Model):
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name="routes",
        related_query_name="route_code",
    )
    name = models.CharField(max_length=10)


# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=120)
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=MAPBOX_API_KEY)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)

class Delivery(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='deliveries')
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    pickup_date = models.DateField(blank=True, null=True)
    pickup_time = models.TimeField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    delivery_time = models.TimeField(blank=True, null=True)
    delivery_image = models.ImageField(upload_to='images/delivery/')

class Driver(models.Model):
    name = models.CharField(max_length=255)
    driver_number = models.IntegerField(null=True, blank=True, max_length=5)
    email = models.EmailField(max_length=255)
    license_number = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    routes = models.ManyToManyField(Route, through='RouteDriver', related_name='drivers')

class RouteDriver(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
