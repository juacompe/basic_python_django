from django.test import TestCase
from thestar.models import Competitor

class TestVoteScreen(TestCase):
    def test_get_vote_screen(self):
        dee = Competitor()
        dee.name = 'Delilian Alford'
        dee.nick_name = 'Dee'
        dee.no = 1
        dee.save()
        
        url = '/'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Delilian Alford')

