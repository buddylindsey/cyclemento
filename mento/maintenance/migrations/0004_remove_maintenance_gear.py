# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0003_auto_20150208_0141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='gear',
        ),
    ]
