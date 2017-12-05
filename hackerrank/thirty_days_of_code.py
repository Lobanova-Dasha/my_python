# thirty_days_of_code.py

# Day 4: Class vs. Instance 
# Task. Write a Person class with an instance variable, age, 
# and a constructor that takes an integer, initialAge, as a parameter. 
# The constructor must assign initialAge to age after confirming 
# the argument passed as initialAge is not negative; 
# if a negative argument is passed as initialAge, 
# the constructor should set age to 0  
# and print Age is not valid, setting age to 0..


class Person:

    def __init__(self,initialAge):
        
        self.age = 0

        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge


    def amIOld(self):
        
        if age < 13:
            print('You are young.')
        elif 13<=age<18:
            print('You are a teenager.')
        else:
            print('You are old.')   
        

    def yearPasses(self):
        # Increment the age of the person in here global age
        age += 1 


t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")  


# Day 5: Loops
# Task.Given an integer,n, print its first 10 multiples. 
# Each multiple should be printed on a new line 
# in the form: n x i = result.

n = int(input())
for i in range(1,11):
    print('{} x {} = {}'.format(n, i, i*n))           


# Day 6: Let's Review
# Task. Given a string,S, of length N that is indexed from 0 to N-1, 
# print its even-indexed and odd-indexed characters as  space-separated 
# strings on a single line 
# Sample Input    Sample Output
# 2
# Hacker          Hce akr
# Rank            Rn ak

for i in range(int(input())):
    word = input()
    even = [word[let] for let in range(len(word)) if let%2 == 0]
    odd = [word[let] for let in range(len(word)) if let%2 == 1]
    print(''.join(even) + ' ' + ''.join(odd))


# I think, it's such genius solution, 
# unfortunately not mine. But I'll memorise this trick
for i in range(int(input())):
    word = input()
    print(word[::2], word[1::2])    

# My first and awful attempt
# n = int(input())
# even = []
# odd = []

# for i in range(n):
#     word = input()
#     for let in range(len(word)):
#         if let%2 == 0:
#             even.append(word[let])
#         else:
#             odd.append(word[let])    
#     print(''.join(even) + ' ' + ''.join(odd))
#     even, odd = [], []

# Python2
# t = int(raw_input())
# for _ in range(t):
#     line = raw_input()
#     first = ""
#     second = ""

#     for i, c in enumerate(line):
#         if (i & 1) == 0:
#             first += c
#         else:
#             second += c
#     print first, second


# Day 7: Arrays 
# Task. Given an array,A, of N integers, print A's elements 
# in reverse order as a single line of space-separated numbers.
usless_arg = input()
print(' '.join(input().split()[::-1]))


# Day 8: Dictionaries and Maps
# Task. Given  names and phone numbers, assemble a phone book 
# that maps friends' names to their respective phone numbers. 
# You will then be given an unknown number of names to query your 
# phone book for. For each name queried, print the associated entry 
# from your phone book on a new line in the form name=phoneNumber; 
#if an entry for name is not found, print "Not found" instead.

n = int(input())
book = dict(input().split() for person in range(n))

# book = {'sam': '99912222',
#         'tom': '11122222',
#         'harry': '12299933'}

for i in range(n):
    name = input()
    number = book.get(name)

    if name in book:
        print(name+'='+number)
    else:
        print('Not found') 


# Day 9: Recursion
# Task. Write a factorial function that takes N a positive integer,  
# as a parameter and prints the result of N! (N factorial).
factorial = lambda x : 1 if x<=1 else x*factorial(x-1)

print(factorial(int(input())))               

# Day 10: Binary numbers

print(len(max(bin(int(input().strip()))[2:].split('0'))))
# line = bin(int(input()))
# print(line)

# num = 0

# if "0" and '1' in line:
#     num += 2
# elif "1" in line:
#     num +=1
# elif "0" in line:
#     num +=1    
# else:
#     pass 

# print(num) 


# Day 12: Inheritance
class Person:
    def __init__(self, firstName, lastName, idNum):
        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum


    def printPerson(self):
        print("Name: {}, {}".format(self.lastName, self.firstName))
        print("ID: {}".format(self.idNum))
            

class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        super().__init__(firstName, lastName, idNum)
        self.scores = scores


    def calculate(self):
        #scores= list(map(int, scores.split()))
        avr = sum(scores) // int(numScores)
        
        if 90<=avr<=100:
            return "O"

        elif 80<=avr<90:
            return "E"
            
        elif 70<=avr<80:
            return "A"
           
        elif 55<=avr<70:
            return "P"
            
        elif 40<=avr<55:
            return "D"
            
        elif avr<40:
            return "T"

# line = input().split()
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]
# numScores = int(input()) # not needed for Python
# scores = list( map(int, input().split()) )
# s = Student(firstName, lastName, idNum, scores)
# s.printPerson()
# print("Grade:", s.calculate())


# Day 13: Abstract Classes 
from abc import ABCMeta, abstractmethod

class Book(metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title = title
        self.author = author   
    
    @abstractmethod
    def display(): 
        pass


class MyBook(Book):
    def __init__(self,title,author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Price: {}".format(self.price))            


# title = input()
# author = input()
# price = int(input())
# new_novel = MyBook(title,author, price)
# new_novel.display()                             


#Day 14: Scope 
def computeDifference(self):
        self.maximumDifference = max(a) - min(a)

#Day 15: Linked List
print(*[input() for x in range(int(input()))])
  

#Day 16: Exceptions - String to Integer
try:
    print(int(input()))

except ValueError as e:
    print('Bad String')
    

# Day 17: More Exceptions 
for i in range(int(input())):
    
    try:
        n,p = map(int, input().split())
        assert n>= 0 and p>=0, "n and p should be non-negative"
        print(n**p)
    
    except Exception as e:
        print(e)


# Day 24: More Linked Lists
a_list = list({int(input()) for i in range(int(input()))})
#a_list.sort()  
print(*(sorted(a_list)))


# Day 25: Running Time and Complexity
from math import factorial

def prime(n):
    if (factorial(n-1)+1) % n!=0:
        print("Not prime")
    else:
        print("Prime")

for x in range(0, int(input())):
    prime(int(input()))        


# # another way    
import math

def is_prime(n):
    if n == 2:
        return True
    elif n == 1 or (n & 1) == 0:
        return False
        
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    
    return True

p = int(input())
for i in range(0, p):
    x = int(input())

    s = "Prime" if (is_prime(x)) else "Not prime"
    print(s)
    
  
# Day 26: Nested Logic
import sys

inlist = sys.stdin.readlines()
ad, am, ay = map(int, inlist[0].strip().split())
ed, em, ey = map(int, inlist[1].strip().split())

if ay > ey: 
    print(10000)
elif ay == ey and am > em: 
    print((am-em)*500)
elif ay == ey and am == em and ad > ed: 
    print((ad-ed)*15)
else: 
    print(0)


# Compare the Triplets
alice = list(map(int, input().split()))
bob = list(map(int, input().split()))

pairs = list(zip(alice, bob))

arr1 = []
arr2 = []

def compair(pair):
 
    if pair[0] > pair[-1]:
        arr1.append(1)
    elif pair[0] < pair[-1]:
        arr2.append(1)
    

# Diagonal Difference
Create a matrix
arr = [list(map(int, input().split())) for x in range(int(input()))]
# get sum of each diagonal  
diag1 = sum([i[arr.index(i)] for i in arr])
diag2 = sum([i[::-1][arr.index(i)] for i in arr])

print(abs(diag1-diag2))


# Given an array of integers, 
# calculate which fraction of its elements are positive, 
# which fraction of its elements are negative, and 
# which fraction of its elements are zeroes, respectively. 
# Print the decimal value of each fraction on a new line.
size = int(input())
numbers = list(map(int, input().split()))
positive = len(list(filter(lambda x: x > 0, numbers)))
negative = len(list(filter(lambda x: x < 0, numbers)))
zeroes = len(list(filter(lambda x: x == 0, numbers)))

for num in (positive, negative, zeroes):
    print(round(num/size, 6))

           
    