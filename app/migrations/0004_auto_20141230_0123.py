# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20141229_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalsufficiency',
            name='id',
            field=models.CharField(default='818cfb36-8fc2-11e4-9b7f-0c8bfd746ca1', primary_key=True, max_length=64, serialize=False),
            preserve_default=True,
        ),
    ]
