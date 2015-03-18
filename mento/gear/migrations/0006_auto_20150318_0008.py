# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0005_auto_20150301_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='total_elevation_gain',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gear',
            name='total_elevation_gain_unit',
            field=models.CharField(blank=True, max_length=5, null=True, choices=[(b'm', b'Meter'), (b'ft', b'Foot'), (b'mi', b'Miles'), (b'km', b'Kilomieter')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gear',
            name='distance',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
