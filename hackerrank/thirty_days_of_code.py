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

