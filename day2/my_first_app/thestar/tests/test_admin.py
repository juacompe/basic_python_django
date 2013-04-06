from django.test import TestCase

class TestCompetitorAdmin(TestCase):
    def test_list_page(self):
        url = '/admin/thestar/competitor/'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

