from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FAQ
from .serializers import FAQSerializer


@api_view(['GET',])
def faq_list(request):
    faqs = FAQ.objects.all()
    return Response(FAQSerializer(faqs, many=True).data)
