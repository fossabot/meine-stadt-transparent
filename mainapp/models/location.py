from django.db import models
from djgeojson.fields import GeometryField

from .default_fields import DefaultFields


class Location(DefaultFields):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    # Need to work around a cyclic import here
    bodies = models.ManyToManyField("mainapp.Body", blank=True)
    is_official = models.BooleanField()
    osm_id = models.BigIntegerField(null=True, blank=True)
    geometry = GeometryField(default=None)

    def __str__(self):
        return self.short_name

    def coordinates(self):
        if self.geometry and self.geometry['type'] == 'Point':
            return {
                "lat": self.geometry['coordinates'][1],
                "lon": self.geometry['coordinates'][0],
            }
        else:
            return None
