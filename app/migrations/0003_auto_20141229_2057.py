# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141229_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalsufficiency',
            name='attorney',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='legalsufficiency',
            name='id',
            field=models.CharField(default='45961a80-8f9d-11e4-82e7-80e650264adc', max_length=64, primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
