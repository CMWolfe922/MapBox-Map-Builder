# BUILDING A MAPPING APP FOR DRIVER ROUTING

---

[ ] TODO: Get the mapbox API to show up using the Django view.
[ ] TODO: Get markers to show up from the input addresses

```javascript
        {% for address in addresses %}
        var marker = new mapboxgl.Marker()
            .setLngLat(['{{ address.long }}', '{{ address.lat }}'])
            .addTo(map);
        {% endfor %}
```

[ ] TODO: Build the address form
