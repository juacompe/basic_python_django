from sample2 import f
from unittest import TestCase

class TestF(TestCase):
    def test_input_is_a(self):
        result = f('a')
        self.assertEqual('the input is a', result)

    def test_input_is_b(self):
        result = f('b')
        self.assertEqual('the input is b', result)

    def test_input_is_c(self):
        result = f('c')
        self.assertEqual('the input is c', result)

