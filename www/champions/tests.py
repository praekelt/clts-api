from django.test import TestCase
from django.db import IntegrityError

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Champion

class ChampionApiTest(APITestCase):

    def setUp(self):
        Champion.objects.create(name='Mr Dijkstra', msisdn='1234567890')
        Champion.objects.create(name='Mr Turing', msisdn='0987654321')

    def test_msisdn_is_unique(self):
        with self.assertRaises(IntegrityError):
            Champion.objects.create(name='Doppel Dijkstra', 
                                    msisdn='1234567890')

    def test_activate_champion_via_api(self):
        url = reverse('champion-activate', args=('0987654321',))
        response = self.client.post(url, None, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    