# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0007_auto_20150327_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(related_name='activities', to=settings.AUTH_USER_MODEL),
        ),
    ]
