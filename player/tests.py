from django.test import TestCase, Client


# Create your tests here.
from player.models import Statistic


class AuthorTestCase(TestCase):

    fixtures = ['fixtures.json']

    def setUp(self):
        self.client = Client()

    def test_get_status_code(self):
        response = self.client.get('/player/author/')
        self.assertEqual(response.status_code, 200)

    def test_get_incorrect_response(self):
        response = self.client.get('/player/author/')
        self.assertEqual(response.data, {"response": 200})

    def test_get_response(self):
        response = self.client.get('/player/author/')
        self.assertEqual(response.data, {"response": 200, "data": 111})
