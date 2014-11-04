from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from json import loads

from snippets.models import Snippet

class TestSnippetAPI(TestCase):
    def setUp(self):
        owner = User.objects.create_user('juacompe', 'email@example.com', 'secret')
        snippet = Snippet(code='foo = "bar"\n', owner=owner)
        snippet.save()

        snippet = Snippet(code='print "hello, world"\n', owner=owner)
        snippet.save()

    def test_list_snippets(self):
        response = self.client.get('/snippets/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        json = loads(response.content)
        self.assertEqual(1, json[0]['id'])
        self.assertEqual('foo = "bar"\n', json[0]['code'])
        self.assertEqual(2, json[1]['id'])
        self.assertEqual('print "hello, world"\n', json[1]['code'])

    def test_get_snippet_detail(self):
        response = self.client.get('/snippets/1/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        json = loads(response.content)
        self.assertEqual('python', json['language'])

    def test_post_snippet(self):
        self.client.login(username='juacompe', password='secret')
        response = self.client.post('/snippets/', {'code':'print 789'})
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_annonymous_post_snippet(self):
        response = self.client.post('/snippets/', {'code':'print 789'})
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
