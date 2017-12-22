# coding: utf-8
#! python 2.7
# even_iterator.py

"""
Напишите итератор EvenIterator, который позволяет получить из списка
все элементы, стоящие на чётных индексах.
"""


class EvenIterator(object):
    
    def __init__(self, seq):
        self.seq = seq
		
    def __iter__(self):
        return self	

    def __getitem__(self, index):
        result = self.seq[index]
        if index%2 == 0:
            return result		
        	
  

items = EvenIterator([5, 17, 23, -5])
print(next(items))
  
		

# ---------------------------------------
# Тесты для проверки правильности решения

"""
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
"""