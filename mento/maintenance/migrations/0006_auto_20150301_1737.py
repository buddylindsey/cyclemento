# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0005_maintenance_gear'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maintenance',
            options={'ordering': ['-created'], 'get_latest_by': 'created', 'verbose_name': 'maintenance', 'verbose_name_plural': 'maintenance'},
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='gear',
            field=models.ForeignKey(related_name='maintenance', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='gear.Gear', null=True),
            preserve_default=True,
        ),
    ]
