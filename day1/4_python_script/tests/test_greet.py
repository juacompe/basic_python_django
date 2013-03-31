from greet import greet
from unittest import TestCase

class TestGreet(TestCase):
    def test_greet_john(self):
        result = greet('John')
        self.assertEqual('Hi John!', result)

    def test_greet_jack(self):
        result = greet('Jack')
        self.assertEqual('Hi Jack!', result)

