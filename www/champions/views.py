from django.http import HttpResponse

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ChampionSerializer
from .models import Champion


class ChampionViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer
    lookup_field = 'msisdn'

    def list(self, request, msisdn=None):
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['POST',])
    def activate(self, request, msisdn=None):
        try:
            champion = Champion.objects.get(msisdn=msisdn)
            champion.activate()
        except Champion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        s = ChampionSerializer(champion, context={'request': request})
        return Response(s.data)
