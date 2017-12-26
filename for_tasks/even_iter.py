# coding: utf-8
#! python 2.7
# even_iter.py

"""
Напишите итератор EvenIterator, который позволяет получить из списка
все элементы, стоящие на чётных индексах.
"""


class EvenIterator(object):

    def __init__(self, sequence):
        self.index = 0
        self.seq = sequence

    def __iter__(self):
        return self

    def next(self):
        if self.index < len(self.seq):
            i = self.index
            self.index += 2
            return self.seq[i]
        else:    
            raise StopIteration()
        

# ---------------------------------------
# Тесты для проверки правильности решения


import unittest


class EvenIteratorTest(unittest.TestCase):

    def test_first_item(self):
        i = EvenIterator([1, 2, 3, 4])

        self.assertEqual(next(i), 1)

    def test_items(self):
        items = list(EvenIterator([5, 17, 23, -5]))

        self.assertListEqual(items, [5, 23])

    def test_empty_list(self):
        items = list(EvenIterator([]))

        self.assertListEqual(items, [])


unittest.main()
