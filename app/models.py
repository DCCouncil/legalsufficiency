from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

# class Office(models.Model):
#     pass

# class Request(models.Model):
#     pass

published = [('draft','Draft'), ('review','Review'),('published','Published')]
m_type = [('B','Bill'),('pr','Proposed Resolution')]

members = [('PM','Chairman Phil Mendelson'),('BN','Councilmember Brianne Nadeau'), ('JE','Councilmember Jack Evans'),('MC','Councilmember Mary Cheh'),('KM','Councilmember Kenyan McDuffie'),('CA','Councilmember Charles Allen'),('YA','Councilmember Yvette Alexander'),('VO','Councilmember Vincent Orange'),('AB','Councilmember Anita Bonds'),('DG','Councilmember David Grosso'),('ES','Councilmember Elissa Silverman')]

class LegalSufficiency(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=str(uuid.uuid1()))
    # request = models.ForeignKey('Request', blank=True, null=True)
    office = models.CharField(max_length=400, choices=members, default='pm')
    attorney = models.ForeignKey(User, unique=True, blank=True, null=True)
    measure_type = models.CharField(max_length=5, choices=m_type, default='b')
    measure_number = models.CharField(max_length=64, null=True, blank=True)
    short_title = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(max_length=10, choices=published, default='draft')
    content = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return '/suff/%s' % self.id