# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('source', models.CharField(max_length=100, choices=[(b'mento', b'CycleMento'), (b'strava', b'Strava'), (b'runkeeper', b'RunKeeper')])),
                ('external_id', models.CharField(max_length=100, null=True, blank=True)),
                ('activity_type', models.CharField(max_length=50, null=True, blank=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('distance', models.FloatField(default=0.0)),
                ('moving_time', models.FloatField(default=0.0)),
                ('elapsed_time', models.FloatField(default=0.0)),
                ('total_elevation_gain', models.FloatField(default=0.0)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('timezone', models.CharField(max_length=25, null=True, blank=True)),
                ('location_city', models.CharField(max_length=255, null=True, blank=True)),
                ('location_state', models.CharField(max_length=255, null=True, blank=True)),
                ('location_country', models.CharField(max_length=255, null=True, blank=True)),
                ('trainer', models.BooleanField(default=False)),
                ('commute', models.BooleanField(default=False)),
                ('manual', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=False)),
                ('flagged', models.BooleanField(default=False)),
                ('user', models.ForeignKey(related_name='activties', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
    ]
