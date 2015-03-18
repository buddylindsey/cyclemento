from django.db import models

from model_utils import Choices


class DistanceModel(models.Model):
    DISTANCE_UNITS = Choices(
        ('m','Meter'), ('ft', 'Foot'), ('mi', 'Miles'), ('km', 'Kilometer'))

    distance = models.FloatField(default=0.0, blank=True, null=True)
    distance_unit = models.CharField(
        max_length=5, blank=True, null=True, choices=DISTANCE_UNITS)

    total_elevation_gain = models.FloatField(default=0.0)
    total_elevation_gain_unit = models.CharField(
        max_length=5, blank=True, null=True, choices=DISTANCE_UNITS)

    class Meta:
        abstract = True

    def calculate_distance(self, distance, unit='m'):
        units = {'m': 0.000621371, 'ft': 0.000189394, 'mi': 1, 'km': 0.621371}
        return round(distance * units.get(unit, 1), 1)

