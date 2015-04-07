# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def create_distance_settings(apps, schema_editor):

    User = apps.get_model('auth', 'User')
    DistanceSettings = apps.get_model('core', 'DistanceSettings')

    for user in User.objects.all():
        DistanceSettings.objects.create(user=user)

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_distance_settings)
    ]
