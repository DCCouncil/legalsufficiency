# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20141230_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='legalsufficiency',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='legalsufficiency',
            name='id',
            field=models.CharField(default='dd24b912-9052-11e4-82e7-80e650264adc', primary_key=True, max_length=64, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='legalsufficiency',
            name='measure_type',
            field=models.CharField(default='B', choices=[('B', 'Bill'), ('PR', 'Proposed Resolution')], max_length=5),
            preserve_default=True,
        ),
    ]
