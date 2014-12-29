# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalSufficiency',
            fields=[
                ('id', models.CharField(default='a636b846-8f63-11e4-a945-80e650264adc', primary_key=True, serialize=False, max_length=64)),
                ('office', models.CharField(default='pm', max_length=400, choices=[('PM', 'Chairman Phil Mendelson'), ('BN', 'Councilmember Brianne Nadeau'), ('JE', 'Councilmember Jack Evans'), ('MC', 'Councilmember Mary Cheh'), ('KM', 'Councilmember Kenyan McDuffie'), ('CA', 'Councilmember Charles Allen'), ('YA', 'Councilmember Yvette Alexander'), ('VO', 'Councilmember Vincent Orange'), ('AB', 'Councilmember Anita Bonds'), ('DG', 'Councilmember David Grosso'), ('ES', 'Councilmember Elissa Silverman')])),
                ('measure_type', models.CharField(default='b', max_length=5, choices=[('B', 'Bill'), ('pr', 'Proposed Resolution')])),
                ('measure_number', models.CharField(null=True, max_length=64, blank=True)),
                ('status', models.CharField(default='draft', max_length=10, choices=[('draft', 'Draft'), ('review', 'Review'), ('published', 'published')])),
                ('content', models.TextField(null=True, blank=True)),
                ('attorney', models.ForeignKey(null=True, unique=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='legalsufficiency',
            name='request',
            field=models.ForeignKey(null=True, blank=True, to='app.Request'),
            preserve_default=True,
        ),
    ]
