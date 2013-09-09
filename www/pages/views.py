from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Page
from .serializers import PageSerializer


@api_view(['GET',])
def pages_list(request, category_slug):
    pages = Page.objects.filter(category__slug=category_slug)
    return Response(PageSerializer(pages, many=True).data)
