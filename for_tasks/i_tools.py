# coding: utf-8
# i_tools.py - creating iterators for efficient looping
#! python 2.7

import itertools as it

arr = xrange(10)

# Chain 
for i in it.chain("ABCD", "1234"):
    print(i)

# The same
for elem in ("ABCD", "1234"):
    for i in elem:
        print i

# Prodact
for i in it.product('1234', 'ABCD'):
    print i

# The same
for num in "1234":
    for let in "ABCD":
        print(num, let)    	


# Combinations
for i in it.combinations(arr, 3):
    print(i)

for i in it.combinations_with_replacement(arr, 4):
    print(i)

#Compress (data, selectors)
for i in it.compress("hello world", [1, 1, 0, 0, 0, 0, 1]):
    print(i)

#Dropwhile
for i in it.dropwhile(lambda x: x < 4, arr):
    print(i)


# Groupby
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"),
          ("vehicle", "speed boat"), ("vehicle", "school bus")]


for key, group in it.groupby(things, lambda x: x[0]):
    for thing in group:
        print("A {} is a {}.".format(thing[1], key))
    print("")


