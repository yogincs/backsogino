from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Subscriber, Suggestion


class ApiTests(TestCase):
    def test_subscribe_email(self):
        response = self.client.post(reverse('email-subscribe'), {'email': 'test@example.com'}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Subscriber.objects.filter(email='test@example.com').exists())

    def test_suggestion_create(self):
        response = self.client.post(reverse('suggestion-create'), {'email': 'test@example.com', 'message': 'Hello'}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Suggestion.objects.filter(email='test@example.com', message='Hello').exists())
