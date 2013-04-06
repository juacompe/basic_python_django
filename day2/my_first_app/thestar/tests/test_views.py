from django.test import TestCase
from thestar.models import Competitor, Vote

class TestVoteScreen(TestCase):
    def test_get_home_page(self):
        dee = Competitor()
        dee.name = 'Delilian Alford'
        dee.nick_name = 'Dee'
        dee.no = 1
        dee.save()
        
        url = '/'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Dee')

    def test_vote(self):
        dee = Competitor()
        dee.name = 'Delilian Alford'
        dee.nick_name = 'Dee'
        dee.no = 1
        dee.save()

        url = '/thestar/vote/?no=1'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        number_of_votes_for_dee = Vote.objects.all().count()
        self.assertEqual(1, number_of_votes_for_dee)

