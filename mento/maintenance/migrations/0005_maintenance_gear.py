# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0004_remove_gear_maintenance'),
        ('maintenance', '0004_remove_maintenance_gear'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='gear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='gear.Gear', null=True),
            preserve_default=True,
        ),
    ]
