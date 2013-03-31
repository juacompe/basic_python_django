from hello_world3 import hello_world
from unittest import TestCase

class TestHelloWorld3(TestCase):
    def test_hello_world(self):
        result = hello_world()
        self.assertEqual('hello world!', result)

