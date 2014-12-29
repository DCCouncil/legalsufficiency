# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='legalsufficiency',
            name='short_title',
            field=models.CharField(null=True, max_length=300, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='legalsufficiency',
            name='id',
            field=models.CharField(serialize=False, primary_key=True, max_length=64, default='e10e7c68-8f6d-11e4-ad16-80e650264adc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='legalsufficiency',
            name='status',
            field=models.CharField(default='draft', max_length=10, choices=[('draft', 'Draft'), ('review', 'Review'), ('published', 'Published')]),
            preserve_default=True,
        ),
    ]
