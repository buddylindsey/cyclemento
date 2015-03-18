from django.db import models

from django_extensions.db.models import TimeStampedModel

from activities.models import Activity
from core.models import DistanceModel
from maintenance.models import Maintenance


class Gear(DistanceModel, TimeStampedModel):
    user = models.ForeignKey('auth.User', related_name='gear')
    external_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    primary = models.BooleanField(default=False)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    model_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        get_latest_by = "created"
        ordering = ['-created']
        verbose_name = verbose_name_plural = 'gear'

    def __unicode__(self):
        return "{} {}".format(self.user.username, self.name)

    def update_with_strava(self, gear):
        self.name = gear.name
        self.distance = gear.distance
        self.distance_unit = gear.distance.get_unit().specifier
        self.primary = gear.primary
        self.brand_name = gear.brand_name
        self.model_name = gear.model_name
        self.description = gear.description

        self.save()

        return self

    def activity_distance(self, activities=None):
        acts = self.activities

        if activities is not None:
            acts = activities

        data = [self.calculate_distance(
            a['distance'], a['distance_unit']) for a in acts.values(
                'distance', 'distance_unit')]
        return sum(data)

    def distance_since_last_maintenance(self):
        try:
            main = self.maintenance.latest()
        except Maintenance.DoesNotExist:
            return 0

        activities = Activity.objects.filter(
            start_date__gt=main.activity.start_date, gear=self)
        return self.activity_distance(activities=activities)


class Compontent(TimeStampedModel):
    gear = models.ForeignKey('gear.Gear', related_name='compontents')
    name = models.CharField(max_length=255, blank=True, null=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)
    distance = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return "{} {}".format(self.gear.name, self.name)
