# BUILDING A MAPPING APP FOR DRIVER ROUTING

---

> When adding date and time information in Django templates, I need to use the date filter like this:
> `{{ value | date 'letters for formating' }}`

- for date, use: 'd m Y' leading zeroes in date format 09-08-2023
  `{{ value | time 'letters for formatting' }}`
- for time use: 'H i s' 24 hour display 16:01:32

[ ] TODO: Get the mapbox API to show up using the Django view.
[ ] TODO: Get markers to show up from the input addresses

```javascript
        {% for address in addresses %}
        var marker = new mapboxgl.Marker()
            .setLngLat(['{{ address.long }}', '{{ address.lat }}'])
            .addTo(map);
        {% endfor %}
```

- This adds controls to the mapbox map.

```javascript
// Add the control to the map.
map.addControl(
  new MapboxGeocoder({
    accessToken: mapboxgl.accessToken,
    mapboxgl: mapboxgl,
  })
);
```

[ ] TODO: Build the address form
[ ] TODO: Add the time since pickup tag when displaying all the deliveries on the board. `{{ delivery|timesince:pickup_time }}`
[ ] I can also use the timeuntil filter for time until pickup is ready. `{{ delivery|timeuntil:pickup }}`

[ ] TODO: Create an index file that will act as the "base" for all templates and will contain the login/signup links

##### Open API Question Responses:

---

- How should a Route model and a Delivery model be related in a database?

> In a database, a Route model and a Delivery model could be related through a foreign key relationship. The Route model could have a one-to-many relationship with the Delivery model, where one route can have multiple deliveries associated with it. The foreign key in the Delivery model would reference the primary key of the associated Route model. This way, when querying the database for deliveries, the associated route information can also be retrieved by joining the two tables on the foreign key.

- How should a Route model and a Driver Model be associated?

> In a database, a Route model and a Driver model could be associated through a many-to-many relationship, since a driver can have multiple routes, and a route can have multiple drivers. One way to implement this relationship is to create a separate table called "Route_Driver" which would have foreign keys to both the Route and Driver tables.
> This table would have a composite primary key made up of both foreign keys. This way, when querying the database for a specific driver, you can easily find all the routes that the driver is assigned to and similarly when querying for a specific route, you can easily find all the drivers assigned to that route.

- how should Route, Driver, and Delivery models be created in Django's models file?

> In Django, you can create the Route, Driver, and Delivery models in the models.py file of your app. Each model should be a subclass of django.db.models.Model and should have fields that correspond to the columns in the database table that will be created for that model.

> For example, the Route model could have fields such as name, start_time, and end_time, while the Driver model could have fields such as name, license_number, and phone_number.

> To establish the relationship between the Route and Delivery models, you can use a ForeignKey field in the Delivery model that references the primary key of the Route model.

> To establish the many-to-many relationship between the Route and Driver models, you can use a ManyToManyField field in both the Route and Driver models that references the other model.

> Here is an example of how these models could be defined:

```python
from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Delivery(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

class Driver(models.Model):
    name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    routes = models.ManyToManyField(Route, through='RouteDriver', related_name='drivers')

class RouteDriver(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
```

> Note that the through='RouteDriver' attribute is used for the ManyToManyField. That's the name of the table that will be created for the many-to-many relationship and also we used related_name='drivers' to access the drivers from route model and routes from driver model.
