# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_legalsufficiency_signator'),
    ]

    operations = [
        migrations.AddField(
            model_name='legalsufficiency',
            name='private',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
