# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_activity_distance_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='total_elevation_gain_unit',
            field=models.CharField(blank=True, max_length=5, null=True, choices=[(b'm', b'Meter'), (b'ft', b'Foot'), (b'mi', b'Miles'), (b'km', b'Kilomieter')]),
            preserve_default=True,
        ),
    ]
