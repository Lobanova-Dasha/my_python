# coding: utf-8
#! python 2.7 - learning map/filter/reduce, modules functools, itertools
# func_prog.py


#Map
names = ['Masha', 'Peter', 'Andrew']

hash_names = map(hash, names)
len_names = map(len, names)
# print(hash_names)
# print({k: v for k, v in zip(hash_names, names)})


# Reduce
my_sum = reduce(lambda a, x: a+x, [x for x in xrange(1, 10+1)])
#print(my_sum)


# Word Count
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

# Count average height
people = [{'name': 'Masha', 'height': 160},
          {'height': 'Sasha', 'height': 180},
          {'name': 'Pasha'}
         ]

heights = map(lambda x: x['height'],
              filter(lambda x: 'height' in x, people))

if len(heights) > 0:
    average_height = reduce(lambda a, x: a+x, heights) / len(heights)

# print average_height



