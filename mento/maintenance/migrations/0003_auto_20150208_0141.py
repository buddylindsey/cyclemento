# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0002_maintenance_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='activities.Activity', null=True),
            preserve_default=True,
        ),
    ]
