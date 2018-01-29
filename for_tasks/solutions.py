#! python 2.7
#solutions.py - from www.codewars.com

#1 https://www.codewars.com/kata/string-incrementer/train/python/5a560ca5d39ec5641400004f
import re

def increment_string(string):
    digits = re.split(r'\D', string)[-1]

    if not digits:
        return string + "1"
    else:    
        value = int(digits) + 1
        return "{}{:0{}}".format(string[:-len(digits)], value, len(digits))
    

#2 https://www.codewars.com/kata/palindrome-chain-length/train/python/5a560bbcd8e145d27c00003c
def palindrome_chain_length(n):
    num = str(n)
    steps = 0

    while num != num[::-1]:
        steps += 1
        num = str(int(num) + int(num[::-1]))
    return steps


#3 https://www.codewars.com/kata/valid-parentheses/train/python/5a55dc9580eba8a39e0000b9
def valid_parentheses(string):
    new_str = filter(lambda x: not x.isalnum(), string)

    for i in xrange(len(new_str) / 2):
       new_str = "".join(new_str.split("()"))

    return not len(new_str)


#4 https://www.codewars.com/kata/valid-braces/train/python/5a55dc38145c469bfd00008f         
def validBraces(string):
    for i in xrange(len(string) / 2):
        string = "".join(string.split("()"))
        string = "".join(string.split("{}"))
        string = "".join(string.split("[]"))
    return not len(string)


#5 https://www.codewars.com/kata/permutations/train/python/5a54b6bffd56cbf3c800003e
from itertools import permutations as perm

def permutations(string):
    return {"".join(i) for i in perm(string, len(string))}


#6 https://www.codewars.com/kata/create-phone-number/train/python/5a464832cadebff3230000a1
def create_phone_number(n):
    n = "".join(map(str, n))
    return "({}) {}-{}".format(n[0:3], n[3:6], n[6::])


#7 https://www.codewars.com/kata/does-my-number-look-big-in-this/train/python/5a46412080eba830e3000062
def narcissistic(value):   
    digits = str(value)
    arr = sum([int(num)**len(digits) for num in digits])
    if arr == value:
        return True
    else:
        return False

#8 https://www.codewars.com/kata/reverse-words/train/python/5a46404cfd56cb744f00007e
def reverse_words(str):
   return " ".join([word[::-1] for word in str.split(" ")])


#9 https://www.codewars.com/kata/counting-duplicates/train/python/5a46396fb3bfa899d0000083
from collections import Counter

def duplicate_count(text):
   
    count_letter = dict(Counter(text.lower()))

    dubls = 0
    for k in count_letter:
        if count_letter[k] > 1:
            dubls += 1
    return dubls


#10 https://www.codewars.com/kata/which-are-in/train/python/5a462d27d8e14594e4000042    
def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})


#11 https://www.codewars.com/kata/sort-the-odd/train/python/5a45f016cadebf366600008a
def sort_array(source_array):

    odd = iter(sorted(filter(lambda x: x % 2, source_array)))
   
    for i in xrange(len(source_array)):
        if source_array[i] % 2:
            source_array[i] = next(odd)
    return source_array


#12 https://www.codewars.com/kata/find-the-divisors/train/python/5a45eed0d8e14541dd00007b
def divisors(integer):

    divs = [x for x in xrange(2, integer) if integer%x == 0]
    if len(divs) == 0:
        return "{} is prime".format(integer)
    else:
        return divs


# the same
def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '{} is prime'.format(n)


#13 https://www.codewars.com/kata/credit-card-mask/train/python/5a45e28580eba818ff000057
# return masked string
def maskify(cc):
    new_s = len(cc[:-4])
    four = cc[-4:]

    if cc <= 4:
        return cc
    else:
        return '#'*new_s + four


#14 https://www.codewars.com/kata/shortest-word/train/python/5a45e18a80eba8424a00004e
def find_short(s):
    return min(map(len, s.split()))



#15 https://www.codewars.com/kata/find-the-parity-outlier/train/python/5a451f04e626c5637200004b
def find_outlier(integers):
    even = filter(lambda x: x%2 == 0, integers)
    odd = filter(lambda x: x%2 == 1, integers)
    return filter(lambda x: len(x) == 1, (even, odd))[0][0]


