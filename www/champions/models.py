from django.utils import timezone
from django.db import models


class Champion(models.Model):
    name = models.CharField(max_length=128)
    msisdn = models.CharField('MSISDN', max_length=18, unique=True)
    eht = models.BooleanField(default=False)
    activated = models.BooleanField(default=False)
    activation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        pass

    def activate(self):
        self.activated = True
        self.activation_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.name


class Village(models.Model):
    name = models.CharField(max_length=128)
    champion = models.ForeignKey('Champion')
    latitude = models.CharField(max_length=16, blank=True)
    longitude = models.CharField(max_length=16, blank=True)
    province = models.CharField(max_length=128, blank=True)
    district = models.CharField(max_length=128, blank=True)
    ward = models.CharField(max_length=128, blank=True)

    class Meta:
        pass

    def __unicode__(self):
        return self.name
