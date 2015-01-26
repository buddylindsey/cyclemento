from django.db import models


from django_extensions.db.models import TimeStampedModel
from model_utils import Choices


class Activity(TimeStampedModel):
    user = models.ForeignKey('auth.User', related_name='activties')

    SOURCES = Choices(
        ('mento', 'CycleMento'), ('strava', 'Strava'),
        ('runkeeper', 'RunKeeper'))

    source = models.CharField(max_length=100, choices=SOURCES)

    external_id = models.CharField(max_length=100, blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    activity_type = models.CharField(max_length=50, blank=True, null=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    distance = models.FloatField(default=0.0)
    moving_time = models.FloatField(default=0.0)
    elapsed_time = models.FloatField(default=0.0)
    total_elevation_gain = models.FloatField(default=0.0)

    start_date = models.DateTimeField(blank=True, null=True)
    timezone = models.CharField(max_length=25, blank=True, null=True)

    location_city = models.CharField(max_length=255, blank=True, null=True)
    location_state = models.CharField(max_length=255, blank=True, null=True)
    location_country = models.CharField(max_length=255, blank=True, null=True)

    trainer = models.BooleanField(default=False)
    commute = models.BooleanField(default=False)
    manual = models.BooleanField(default=False)
    private = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)
