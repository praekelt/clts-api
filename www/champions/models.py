from django.db import models


class CommunityChampion(models.Model):
	name = models.CharField(max_length=128)
	msisdn = models.CharField(max_length=18)

	class Meta:
		pass

	def __unicode__(self):
		return self.name


class Activation(models.Model):
	entered = models.CharField(max_length=32)
	matched = models.ForeignKey('CommunityChampion')
	activation_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		pass

	def __unicode__(self):
		return '%s actived on %s' % (self.matched, self.activation_date)
