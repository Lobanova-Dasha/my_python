#! Python3
# itertools.py

# itertools.product()
# Task. You are given a two lists A and B. 
# Your task is to compute their cartesian product AXB.
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))


# itertools.permutations()
# Task You are given a string S. 
# Your task is to print all possible permutations of size k 
# of the string in lexicographic sorted order.
from itertools import permutations

data, k = input().split()

for item in permutations(sorted(data), int(k)):
    print(''.join(item))

# Python2
# from itertools import *
# S, k = raw_input().split()
# for i in permutations(sorted(S),int(k)):
#     print "".join(i)


# itertools.combinations()
# You are given a string S. 
# Your task is to print all possible combinations, 
# up to size k, of the string in lexicographic sorted order
from itertools import combinations

data, n = input().split()

for i in range(1, int(n)+1):
    for item in combinations(sorted(data), i):
        print(''.join(item))

# Python2
# from itertools import combinations

# data, n  = raw_input().split()

# for i in range(1, int(n)+1):
#     for item in combinations(sorted(data), i):
#         print ''.join(item) 


# itertools.combinations_with_replacement()
# You are given a string S. 
# Your task is to print all possible size k replacement combinations 
# of the string in lexicographic sorted order.
from itertools import combinations_with_replacement

data, k = input().split()

for item in combinations_with_replacement(sorted(data), int(k)):
    print(''.join(item))  

# Python2
# from itertools import combinations_with_replacement

# data, k = raw_input().split()

# for item in combinations_with_replacement(sorted(data), int(k)):
#     print ''.join(item)


# Compress the String!
# You are given a string S. Suppose a character 'c' occurs X
# consecutively  times in the string. 
# Replace these consecutive occurrences of the character 'c' 
# with (X,c) in the string.
# Sample Input  1222311
# Sample Output (1, 1) (3, 2) (1, 3) (2, 1)
from itertools import groupby

print(*[(len(list(c)), int(k)) for k, c in groupby(input())]) 
# The list is built of elements of (len(list(c)), int(k)). 
# len(list(c)) is simply the number of occurences of 
# a character c returned by the groupby function. 
# k is just the key value, the character itself.
# * unpacking the list comprehension and printing each element of it.

# Iterables and Iterators
# You are given a list of N lowercase English letters. 
# For a given integer K, you can select any  K indices 
#(assume 1-based indexing) with a uniform probability from the list.
# Find the probability that at least one 
# of the  indices selected will contain the letter: 'a'.

from itertools import combinations
# If you want to check this code on HR 
# you need to run the next 
# _, data, k = input(), input().split, int(input())
# but locally, it works only in this way: data = input(), without split()
_, data, k = input(), input(), int(input())

comb = list(combinations(data, k))
a_list = [i for i in comb if 'a' in i]
print(len(a_list)/len(comb))


# Maximize It!
from itertools import product

n, denominator = map(int,input().split())
arr = (list(map(int, input().split()))[1:] for _ in range(n))

results = map(lambda x: sum(i**2 for i in x)%denominator, product(*arr))
print(max(results))