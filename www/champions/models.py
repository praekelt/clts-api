from django.utils import timezone
from django.db import models


class Champion(models.Model):
	name = models.CharField(max_length=128)
	msisdn = models.CharField('MSISDN', max_length=18, unique=True)
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