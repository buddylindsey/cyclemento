# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='place',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
