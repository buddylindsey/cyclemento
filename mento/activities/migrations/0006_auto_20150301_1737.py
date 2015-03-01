# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_auto_20150208_0133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['-start_date'], 'get_latest_by': 'start_date', 'verbose_name_plural': 'activities'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_date',
            field=models.DateTimeField(help_text=b'Date you did the ride', null=True, blank=True),
            preserve_default=True,
        ),
    ]
