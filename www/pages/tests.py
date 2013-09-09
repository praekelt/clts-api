from django.utils.simplejson import loads
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Page


class FAQTest(APITestCase):

    def setUp(self):

        self.cat_training = Category.objects.create(name="Training")
        self.cat_sausages = Category.objects.create(name="Sausages")

        Page.objects.create(title="Day", category=self.cat_training)
        Page.objects.create(title="Manual", category=self.cat_training)
        Page.objects.create(title="Rope", category=self.cat_training)

    def test_faqs_response(self):
        url = reverse('pages-list', args=(self.cat_training.slug,))
        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        pages = loads(response.content)
        self.assertEqual(len(pages), 3)
        # self.assertEqual(pages[0]['question'], '?')
        # self.assertEqual(pages[2]['answer'], 'the world.')
