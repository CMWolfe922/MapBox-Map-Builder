import geocoder
from django.db import models


# mapbox.com API key
MAPBOX_API_KEY = "pk.eyJ1IjoiY213b2xmZSIsImEiOiJjbGQxMnFjbTExdWt0M3Z0N2hzZThqZ3luIn0.ZvKlTXVuzS9MZegMWAhGPw"

# Create your models here.
class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=MAPBOX_API_KEY)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)
