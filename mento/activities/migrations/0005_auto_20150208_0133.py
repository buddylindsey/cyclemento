# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_activity_gear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='distance',
            field=models.FloatField(default=0.0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
