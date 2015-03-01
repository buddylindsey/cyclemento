# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0004_remove_gear_maintenance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gear',
            options={'ordering': ['-created'], 'get_latest_by': 'created', 'verbose_name': 'gear', 'verbose_name_plural': 'gear'},
        ),
    ]
