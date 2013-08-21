from rest_framework import serializers

from .models import Champion


class ChampionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Champion
		fields = ('url', 'msisdn', 'name', 'activated', 'activation_date')
		lookup_field = 'msisdn'
