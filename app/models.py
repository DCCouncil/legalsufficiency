from django.db import models
from django.contrib.auth.models import User
import uuid
from redactor.fields import RedactorField
from datetime import date

# Create your models here.

# class Office(models.Model):
#     pass

# class Request(models.Model):
#     pass

published = [('draft','Draft'), ('review','Review'),('published','Published')]
m_type = [('B','Bill'),('PR','Proposed Resolution')]

members = [('PM','Chairman Phil Mendelson'),('BN','Councilmember Brianne Nadeau'), ('JE','Councilmember Jack Evans'),('MC','Councilmember Mary Cheh'),('KM','Councilmember Kenyan McDuffie'),('CA','Councilmember Charles Allen'),('YA','Councilmember Yvette Alexander'),('VO','Councilmember Vincent Orange'),('AB','Councilmember Anita Bonds'),('DG','Councilmember David Grosso'),('ES','Councilmember Elissa Silverman')]

class LegalSufficiency(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=str(uuid.uuid1()))
    # request = models.ForeignKey('Request', blank=True, null=True)
    office = models.CharField(max_length=400, choices=members, default='pm')
    attorney = models.ForeignKey(User, blank=True, null=True)
    measure_type = models.CharField(max_length=5, choices=m_type, default='B')
    measure_number = models.CharField(max_length=64, null=True, blank=True)
    short_title = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(max_length=10, choices=published, default='draft')
    content = RedactorField(verbose_name=u'Content')
    publish_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '%s%s: %s' % (self.measure_type, self.measure_number, self.short_title)

    def get_absolute_url(self):
        return '/suff/%s' % self.id

    def get_public_url(self):
        return '/view/%s' % self.id

    def publish(self):
        self.publish_date = date.today()
        self.status = 'published'

    class Meta:
        permissions = ( 
            ( "can_publish", "Can Publish LSDs" ),
        )