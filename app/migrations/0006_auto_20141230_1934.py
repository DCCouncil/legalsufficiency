# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20141230_1837'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='legalsufficiency',
            options={'permissions': (('can_publish', 'Can Publish LSDs'),)},
        ),
        migrations.AlterField(
            model_name='legalsufficiency',
            name='id',
            field=models.CharField(serialize=False, max_length=64, default='f0a6f27e-905a-11e4-b6e4-80e650264adc', primary_key=True),
            preserve_default=True,
        ),
    ]
