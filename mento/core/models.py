from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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


class DistanceSettings(models.Model):
    user = models.OneToOneField('auth.User')
    default_distance_unit = models.CharField(
        max_length=5, choices=DistanceModel.DISTANCE_UNITS,
        default=DistanceModel.DISTANCE_UNITS.mi)

    def __unicode__(self):
        return "{} - {}".format(self.user.username, self.default_distance_unit)


@receiver(post_save, sender=User)
def distance_settings(sender, **kwargs):
    user = kwargs.get('instance')
    created = kwargs.get('created')
    if created:
        DistanceSettings.objects.create(user=user)
