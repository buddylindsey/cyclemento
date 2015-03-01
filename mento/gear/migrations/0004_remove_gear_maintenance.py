# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0003_gear_maintenance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gear',
            name='maintenance',
        ),
    ]
