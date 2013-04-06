from test_wiki_data import python_text, ruby_text
from unittest import TestCase
from wiki import get_from_wiki, get_first_paragraph

class TestGetFromWikipedia(TestCase):
    def test_get_python_from_wiki(self):
        response = get_from_wiki('Python')
        self.assertEqual(200, response.status_code)
        self.assertEqual(python_text, get_first_paragraph(response.content))

    def test_get_ruby_from_wiki(self):
        response = get_from_wiki('Ruby')
        self.assertEqual(200, response.status_code)
        self.assertEqual(ruby_text, get_first_paragraph(response.content))

