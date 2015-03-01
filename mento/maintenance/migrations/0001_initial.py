# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0002_gear_distance_unit'),
        ('activities', '0005_auto_20150208_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('distance', models.FloatField(default=0.0, null=True, blank=True)),
                ('distance_unit', models.CharField(blank=True, max_length=5, null=True, choices=[(b'm', b'Meter'), (b'ft', b'Foot'), (b'mi', b'Miles'), (b'km', b'Kilomieter')])),
                ('description', models.TextField(blank=True)),
                ('activity', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='activities.Activity')),
                ('gear', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='gear.Gear')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
    ]
