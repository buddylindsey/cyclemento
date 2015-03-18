from django.db import models

from django_extensions.db.models import TimeStampedModel
from model_utils import Choices

from gear.utils import get_strava_gear
from core.models import DistanceModel


class Activity(DistanceModel, TimeStampedModel):
    user = models.ForeignKey('auth.User', related_name='activties')

    SOURCES = Choices(
        ('mento', 'CycleMento'), ('strava', 'Strava'),
        ('runkeeper', 'RunKeeper'))

    source = models.CharField(max_length=100, choices=SOURCES)

    external_id = models.CharField(max_length=100, blank=True, null=True)

    activity_type = models.CharField(max_length=50, blank=True, null=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    moving_time = models.FloatField(default=0.0)
    elapsed_time = models.FloatField(default=0.0)

    start_date = models.DateTimeField(
        blank=True, null=True, help_text="Date you did the ride")
    timezone = models.CharField(max_length=25, blank=True, null=True)

    location_city = models.CharField(max_length=255, blank=True, null=True)
    location_state = models.CharField(max_length=255, blank=True, null=True)
    location_country = models.CharField(max_length=255, blank=True, null=True)

    trainer = models.BooleanField(default=False)
    commute = models.BooleanField(default=False)
    manual = models.BooleanField(default=False)
    private = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)

    gear = models.ForeignKey(
        'gear.Gear', blank=True, null=True, related_name='activities')

    class Meta:
        get_latest_by = "start_date"
        ordering = ['-start_date']
        verbose_name_plural = 'activities'

    def __unicode__(self):
        return "{} - {} - {}".format(
            self.source, self.user.username, self.name)

    def actual_distance(self):
        return self.calculate_distance(self.distance, self.distance_unit)

    def update_with_strava(self, act):
        self.distance = act.distance.get_num()
        self.distance_unit = act.distance.get_unit().specifier
        self.activity_type = self.activity_type

        self.name = act.name
        self.moving_time = act.moving_time.total_seconds()
        self.elapsed_time = act.elapsed_time.total_seconds()
        self.total_elevation_gain = act.total_elevation_gain
        self.total_elevation_gain_unit = \
            act.total_elevation_gain.get_unit().specifier

        self.start_date = act.start_date
        self.timezone = act.timezone.zone

        self.location_city = act.location_city
        self.location_state = act.location_state
        self.location_country = act.location_country

        self.trainer = act.trainer
        self.commute = act.commute
        self.manual = act.manual
        self.private = act.private
        self.flagged = act.flagged


        if act.gear_id:
            self.gear = get_strava_gear(self, act.gear_id)

        self.save()

        return self
