from django.test import TestCase
from thestar import factory
from thestar.models import Competitor, Vote

class TestVoteScreen(TestCase):
    def test_get_home_page(self):
        dee = factory.create_competitor() 
        
        url = '/'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Dee')

    def test_vote(self):
        dee = factory.create_competitor() 

        url = '/thestar/vote/?no=1'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        number_of_votes_for_dee = Vote.objects.count()
        self.assertEqual(1, number_of_votes_for_dee)


class TestCompetitorAPI(TestCase):
    def test_get_competitors(self):
        url = '/thestar/competitors/'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

