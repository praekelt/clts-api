from django.utils.simplejson import loads
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import FAQ


class FAQTest(APITestCase):

    def setUp(self):
        FAQ.objects.create(question="?", answer="42.")
        FAQ.objects.create(question="Woodchuck?", answer="12.")
        FAQ.objects.create(question="Margle", answer="the world.")

    def test_faqs_response(self):
        url = reverse('faqs-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        faqs = loads(response.content)
        self.assertEqual(len(faqs), 3)
        self.assertEqual(faqs[0]['question'], '?')
        self.assertEqual(faqs[2]['answer'], 'the world.')
