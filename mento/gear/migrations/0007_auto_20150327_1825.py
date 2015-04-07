# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0006_auto_20150318_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='distance_unit',
            field=models.CharField(blank=True, max_length=5, null=True, choices=[(b'm', b'Meter'), (b'ft', b'Foot'), (b'mi', b'Miles'), (b'km', b'Kilometer')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gear',
            name='total_elevation_gain_unit',
            field=models.CharField(blank=True, max_length=5, null=True, choices=[(b'm', b'Meter'), (b'ft', b'Foot'), (b'mi', b'Miles'), (b'km', b'Kilometer')]),
            preserve_default=True,
        ),
    ]
