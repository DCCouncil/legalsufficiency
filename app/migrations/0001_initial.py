# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
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
                ('id', models.CharField(max_length=64, default='dec10d4c-8f77-11e4-9944-80e650264adc', primary_key=True, serialize=False)),
                ('office', models.CharField(default='pm', max_length=400, choices=[('PM', 'Chairman Phil Mendelson'), ('BN', 'Councilmember Brianne Nadeau'), ('JE', 'Councilmember Jack Evans'), ('MC', 'Councilmember Mary Cheh'), ('KM', 'Councilmember Kenyan McDuffie'), ('CA', 'Councilmember Charles Allen'), ('YA', 'Councilmember Yvette Alexander'), ('VO', 'Councilmember Vincent Orange'), ('AB', 'Councilmember Anita Bonds'), ('DG', 'Councilmember David Grosso'), ('ES', 'Councilmember Elissa Silverman')])),
                ('measure_type', models.CharField(default='b', max_length=5, choices=[('B', 'Bill'), ('pr', 'Proposed Resolution')])),
                ('measure_number', models.CharField(blank=True, max_length=64, null=True)),
                ('short_title', models.CharField(blank=True, max_length=300, null=True)),
                ('status', models.CharField(default='draft', max_length=10, choices=[('draft', 'Draft'), ('review', 'Review'), ('published', 'Published')])),
                ('content', redactor.fields.RedactorField(verbose_name='Content')),
                ('attorney', models.ForeignKey(unique=True, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
