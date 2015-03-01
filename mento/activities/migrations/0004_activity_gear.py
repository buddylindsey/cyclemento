# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0001_initial'),
        ('activities', '0003_activity_total_elevation_gain_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='gear',
            field=models.ForeignKey(related_name='activities', blank=True, to='gear.Gear', null=True),
            preserve_default=True,
        ),
    ]
