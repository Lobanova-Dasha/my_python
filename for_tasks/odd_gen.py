# coding: utf-8
#! python 2.7
# odd_gen.py
import types
import unittest


def odd_generator(n):
    """Returns all odd numbers (1-n)"""

    for x in xrange(1, n+1):
        if x%2 == 1:
            yield x        


class OddGeneratorTest(unittest.TestCase):

    def test_is_generator(self):
        g = odd_generator(4)

        self.assertIsInstance(g, types.GeneratorType)

    def test_first_item(self):
        g = odd_generator(4)

        self.assertEqual(next(g), 1)

    def test_items(self):
        items = list(odd_generator(7))

        self.assertListEqual(items, [1, 3, 5, 7])

    def test_n_less_than_1(self):
        items = list(odd_generator(0))

        self.assertListEqual(items, [])


unittest.main()        