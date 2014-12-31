# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalSufficiency',
            fields=[
                ('slug', models.SlugField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('office', models.CharField(max_length=400, default='pm', choices=[('PM', 'Chairman Phil Mendelson'), ('BN', 'Councilmember Brianne Nadeau'), ('JE', 'Councilmember Jack Evans'), ('MC', 'Councilmember Mary Cheh'), ('KM', 'Councilmember Kenyan McDuffie'), ('CA', 'Councilmember Charles Allen'), ('YA', 'Councilmember Yvette Alexander'), ('VO', 'Councilmember Vincent Orange'), ('AB', 'Councilmember Anita Bonds'), ('DG', 'Councilmember David Grosso'), ('ES', 'Councilmember Elissa Silverman')])),
                ('measure_type', models.CharField(max_length=5, default='B', choices=[('B', 'Bill'), ('PR', 'Proposed Resolution')])),
                ('measure_number', models.CharField(max_length=64, blank=True, null=True)),
                ('short_title', models.CharField(max_length=300, blank=True, null=True)),
                ('status', models.CharField(max_length=10, default='draft', choices=[('draft', 'Draft'), ('review', 'Review'), ('published', 'Published')])),
                ('content', redactor.fields.RedactorField(verbose_name='Content')),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('attorney', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
            options={
                'permissions': (('can_publish', 'Can Publish LSDs'),),
            },
            bases=(models.Model,),
        ),
    ]
