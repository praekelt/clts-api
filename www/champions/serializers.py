from rest_framework import serializers

from .models import Champion, Village


class ChampionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Champion
        fields = ('url', 'msisdn', 'name', 'activated', 'activation_date')
        lookup_field = 'msisdn'


class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        exclude = ('champion',)
