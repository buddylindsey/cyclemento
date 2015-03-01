from django.db import models

from django_extensions.db.models import TimeStampedModel
from model_utils import Choices


class Maintenance(TimeStampedModel):
    activity = models.ForeignKey(
        'activities.Activity', on_delete=models.SET_NULL, null=True,
        blank=True)

    DISTANCE_UNITS = Choices(
        ('m','Meter'), ('ft', 'Foot'), ('mi', 'Miles'), ('km', 'Kilomieter'))

    distance = models.FloatField(default=0.0, blank=True, null=True)
    distance_unit = models.CharField(
        max_length=5, blank=True, null=True, choices=DISTANCE_UNITS)

    description = models.TextField(blank=True)
    place = models.CharField(max_length=255, blank=True)

    gear = models.ForeignKey(
        'gear.Gear', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='maintenance')

    class Meta:
        get_latest_by = "created"
        ordering = ['-created']
        verbose_name = verbose_name_plural = 'maintenance'

    def __unicode__(self):
        return "{} {}".format(self.activity.user.username, self.created)
