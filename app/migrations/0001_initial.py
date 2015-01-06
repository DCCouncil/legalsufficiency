# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalSufficiency',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False, default=uuid.uuid4)),
                ('office', models.CharField(default='pm', max_length=400, choices=[('PM', 'Chairman Phil Mendelson'), ('BN', 'Councilmember Brianne Nadeau'), ('JE', 'Councilmember Jack Evans'), ('MC', 'Councilmember Mary Cheh'), ('KM', 'Councilmember Kenyan McDuffie'), ('CA', 'Councilmember Charles Allen'), ('YA', 'Councilmember Yvette Alexander'), ('VO', 'Councilmember Vincent Orange'), ('AB', 'Councilmember Anita Bonds'), ('DG', 'Councilmember David Grosso'), ('ES', 'Councilmember Elissa Silverman')])),
                ('measure_type', models.CharField(default='B', max_length=5, choices=[('B', 'Bill'), ('PR', 'Proposed Resolution')])),
                ('measure_number', models.CharField(null=True, max_length=64, blank=True)),
                ('short_title', models.CharField(null=True, max_length=300, blank=True)),
                ('amendment', models.BooleanField(default=False)),
                ('amendment_number', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('status', models.CharField(default='draft', max_length=10, choices=[('draft', 'Draft'), ('review', 'Review'), ('published', 'Published')])),
                ('content', redactor.fields.RedactorField(verbose_name='Content')),
                ('publish_date', models.DateField(null=True, blank=True)),
                ('attorney', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'permissions': (('can_publish', 'Can Publish LSDs'),),
            },
            bases=(models.Model,),
        ),
    ]
