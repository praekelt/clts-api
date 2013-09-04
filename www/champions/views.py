from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Champion, Village
from .serializers import ChampionSerializer, VillageSerializer


@api_view(['POST',])
def activate(request, msisdn):
    try:
        champion = Champion.objects.get(msisdn=msisdn)
        champion.activate()
    except Champion.DoesNotExist:
        return Response(status=404)


    villages = Village.objects.filter(champion=champion)
    response = {
        'champion': ChampionSerializer(champion).data,
        'villages': VillageSerializer(villages, many=True).data
    }
    
    return Response(response)

