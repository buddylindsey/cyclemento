# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0004_remove_maintenance_gear'),
        ('gear', '0002_gear_distance_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='maintenance',
            field=models.ForeignKey(blank=True, to='maintenance.Maintenance', null=True),
            preserve_default=True,
        ),
    ]
