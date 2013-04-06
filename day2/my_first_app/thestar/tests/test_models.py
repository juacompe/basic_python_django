from django.db import IntegrityError 
from django.test import TestCase
from thestar import factory
from thestar.models import Competitor

class CompetitorTest(TestCase):
    def test_save_competitor(self):
        dee = Competitor()
        dee.name = 'Delilian Alford'
        dee.nick_name = 'Dee'
        dee.no = 1
        self.assertFalse(dee.id) # before save, no id
        dee.save()
        self.assertTrue(dee.id) # id is auto-generated after saved
        
        dee_id = dee.id
        dee = Competitor.objects.get(id=dee_id)
        self.assertEqual('Delilian Alford', dee.name)
        self.assertEqual('Dee', dee.nick_name)
        self.assertEqual(1, dee.no)

    def test_vote_number_must_be_unique(self):
        dee = factory.create_competitor() 

        chris = Competitor()
        chris.name = 'Christopher Jonathan Roy Chaafe'
        chris.nick_name = 'Chris'
        chris.no = 1
        self.assertRaises(IntegrityError, chris.save)

