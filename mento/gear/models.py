from django.db import models

from django_extensions.db.models import TimeStampedModel


class Gear(TimeStampedModel):
    user = models.ForeignKey('auth.User', related_name='gear')
    external_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    primary =  models.BooleanField(default=False)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    model_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Compontent(TimeStampedModel):
    gear = models.ForeignKey('gear.Gear', related_name='compontents')
    name = models.CharField(max_length=255, blank=True, null=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)
    distance = models.FloatField(blank=True, null=True)
