from django.db import models
from django.contrib.auth.models import User
import uuid
from redactor.fields import RedactorField
from datetime import date
from django.db.models.signals import pre_save
from django.dispatch import receiver
import reversion

# Create your models here.

published = [('draft','Draft'), ('review','Review'),('published','Published')]
m_type = [('B','Bill'),('PR','Proposed Resolution')]
signator = "John Hoellen, Acting General Counsel"
members = [('PM','Chairman Phil Mendelson'),('BN','Councilmember Brianne Nadeau'), ('JE','Councilmember Jack Evans'),('MC','Councilmember Mary Cheh'),('KM','Councilmember Kenyan McDuffie'),('CA','Councilmember Charles Allen'),('YA','Councilmember Yvette Alexander'),('VO','Councilmember Vincent Orange'),('AB','Councilmember Anita Bonds'),('DG','Councilmember David Grosso'),('ES','Councilmember Elissa Silverman')]

@reversion.register
class LegalSufficiency(models.Model):
    slug = models.SlugField(default=uuid.uuid4, primary_key=True)
    office = models.CharField(max_length=400, choices=members, default='pm')
    attorney = models.ForeignKey(User, blank=True, null=True)
    measure_type = models.CharField(max_length=5, choices=m_type, default='B')
    measure_number = models.CharField(max_length=64, null=True, blank=True)
    short_title = models.CharField(max_length=300, null=True, blank=True)
    amendment = models.BooleanField(default=False)
    amendment_number = models.PositiveSmallIntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=published, default='draft')
    content = RedactorField(verbose_name=u'Content')
    publish_date = models.DateField(blank=True, null=True)
    signator = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '%s%s: %s' % (self.measure_type, self.measure_number, self.short_title)

    def get_absolute_url(self):
        return '/suff/%s' % self.slug

    def get_public_url(self):
        return '/view/%s' % self.slug

    def publish(self):
        self.publish_date = date.today()
        self.status = 'published'
        self.signator = signator

    def get_title(self):
        if self.measure_number != "" and self.amendment and self.amendment_number != None:
            return 'Amendment #%s to %s %s, the %s' % (self.amendment_number, self.get_measure_type_display(), self.measure_number, self.short_title)
        elif self.measure_number != "" and self.amendment:
            return 'Amendment to %s %s, the %s' % (self.get_measure_type_display(), self.measure_number, self.short_title)
        elif self.measure_number != "":
            return '%s %s, the %s' % (self.get_measure_type_display(), self.measure_number, self.short_title)
        elif self.amendment:
            return 'Amendment to the %s' % (self.short_title)
        else: 
            return 'the %s' % (self.short_title)

    class Meta:
        permissions = ( 
            ( "can_publish", "Can Publish LSDs" ),
        )

    # @receiver(pre_save)
    # def set_uuid_on_save(sender, instance, *args, **kwargs):
    #     if instance.uid is None:
    #         instance.uid = str(uuid.uuid4())