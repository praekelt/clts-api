from django.db import IntegrityError
from django.utils.simplejson import loads
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Champion, Village


class ChampionTest(APITestCase):

    def setUp(self):

        self.msisdn_1 = '1234567890'
        self.msisdn_2 = '0987654321'
        champ = Champion.objects.create(name='Mr Dijkstra', 
            msisdn=self.msisdn_1)
        Champion.objects.create(name='Mr Turing', msisdn=self.msisdn_2)

        Village.objects.create(champion=champ, name='South Side')
        Village.objects.create(champion=champ, name='East Side')

    def test_msisdn_is_unique(self):
        with self.assertRaises(IntegrityError):
            Champion.objects.create(name='Doppel Dijkstra', 
                                    msisdn=self.msisdn_1)

    def test_activate_champion_via_api(self):
        url = reverse('champion-activate', args=(self.msisdn_2,))
        response = self.client.post(url, None, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        c = Champion.objects.get(msisdn=self.msisdn_2)
        self.assertTrue(c.activated)

    def test_activate_champions_returns_data(self):
        url = reverse('champion-activate', args=(self.msisdn_1,))
        response = self.client.post(url, None, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = loads(response.content)

        self.assertTrue(data['champion']['activated'])

        self.assertEqual(len(data['villages']), 2)
        self.assertEqual(data['villages'][0]['name'], 'South Side')
