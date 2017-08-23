#! python3
# basic_dt.py

# Lists
arr = []
for i in range(int(input())):
    s = input().split()
    for i in range(1,len(s)):
        s[i] = int(s[i])
        
    if s[0] == "append":
        arr.append(s[1])
    elif s[0] == "extend":    
        arr.extend(s[1:])
    elif s[0] == "insert":
        arr.insert(s[1],s[2])
    elif s[0] == "remove":
        arr.remove(s[1])
    elif s[0] == "pop":
        arr.pop()
    elif s[0] == "index":
        print(arr.index(s[1]))
    elif s[0] == "count":
        print(arr.count(s[1]))
    elif s[0] == "sort":
        arr.sort()
    elif s[0] == "reverse":
        arr.reverse()
    elif s[0] == "print":
        print(arr)


#Tuples#
# Type n space-separated integers:
print(hash(tuple([int(i) for i in input().split()])))

# Just for my understanding
#print(hash(tuple([1, 2, 3])))

#List Comprehensions#
# There are three integers X, Y, Z  
# that are representing the dimensions of a cuboid along with an integer 
# I want to create a list of all possible coordinates 
# given by (i, j, k)  on a 3D grid 
# where the sum of i+j+k is not equal to N.

x, y, z, n = [int(input()) for num in range(4)]

possible_coordinates = [[i, j, k] for i in range(x+1) 
                                  for j in range(y+1)
                                  for k in range(z+1)
                                  if ((i+j+k) != n )] 

print(possible_coordinates)  

#The long way with tehe same result
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# ar = []
# p = 0

# for i in range (x+1) :
#     for j in range(y+1):
#     	for k in range(z+1):
#           if i+j+k != n:
#                 ar.append([])
#                 ar[p] = [i, j, k]
#                 p+=1
#
# print(ar) 


#Find the Second Largest Number#
n = input()

a_list = [int(i) for i in input().split()]

print(sorted(list(set(a_list)))[-2])


# Nested Lists#
# Given the names and grades for each student 
# in a Physics class of  students, 
# store them in a nested list and print the name(s) 
#of any student(s) having the second lowest grade.

students = [[input(), float(input())] for person in range(int(input()))]

a_dict = dict(sorted(students))
val = list(a_dict.values())
mark = sorted(list(set(val)))[1]

for k, v in a_dict.items():
	if v == mark:
		print(k)


# Finding the percentage #	
# The first line contains the integer ,the number of students. 
# The next  lines contains the name and marks obtained 
# by that student separated by a space. The final line c
# ontains the name of a particular student previously listed.	

#Import decimal
from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *args = input().split()
        scores = list(map(float, args))
        student_marks[name] = scores
    query_name = input()


# Extract the values into a list: query_scores
query_scores = student_marks[query_name]

# Sum the scores in the list: total_scores
total_scores = sum(query_scores)

# Convert the floats to decimals and average the scores: avg
avg = Decimal(total_scores/3)

# Print the mean of the scores, correct to two decimals
print(round(avg,2))


