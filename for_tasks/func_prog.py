# coding: utf-8
#! python 2.7 
# func_prog.py - - learning map/filter/reduce, module functools


# Map applies a function to all the items in an input_list. Here is the blueprint:
# ex. 1
def add(x):
    return x + x

def mult(x):
    return x*x


funcs = [add, mult]
for i in xrange(10):
    value = map(lambda x: x(i), funcs)
    #print(value)

# ex.2
names = ['Masha', 'Peter', 'Andrew']
hash_names = map(hash, names)
len_names = map(len, names)
# print(hash_names)
# print({k: v for k, v in zip(hash_names, names)})


# Filter creates a list of elements for which a function returns true
# ex. 1
num_list = [x for x in xrange(-100, 100+1)]
less_than_zero = filter(lambda x: x  < 0, num_list)
more_than_zero = filter(lambda x: x > 0, num_list)
#print(more_than_zero)


# Reduce applies a rolling computation to sequential pairs of values in a list.
multiplying = reduce(lambda a, x: a * x, less_than_zero)
#print(multiplying)

my_sum = reduce(lambda a, x: a + x, [x for x in xrange(1, 10+1)])
#print(my_sum)


# 1) Word Count
sentences = ['We wish you a Merry Christmas',
             'We wish you a Merry Christmas',
             'We wish you a Merry Christmas',
             'And a happy New Year'
            ]

word_count = reduce(lambda a, x: a + x.count('happy'), 
	                sentences, 
	                0
	                )

# print(word_count)

# 2) Count average height
people = [{'name': 'Masha', 'height': 160},
          {'height': 'Sasha', 'height': 180},
          {'name': 'Pasha'}
         ]

heights = map(lambda x: x['height'],
              filter(lambda x: 'height' in x, people))

if len(heights) > 0:
    average_height = reduce(lambda a, x: a+x, heights) / len(heights)

# print average_height

