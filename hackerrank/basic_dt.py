#! python3
# basic_dt.py

#Tuples#
#Type n space-separated integers:

#print(hash(tuple([int(i) for i in input().split()])))

# print(hash(tuple([1, 2, 3])))

#List Comprehensions#

# There are three integers X, Y, Z  
# that are representing the dimensions of a cuboid along with an integer 
# I want to create a list of all possible coordinates 
# given by (i, j, k)  on a 3D grid 
# where the sum of i+j+k is not equal to N.

# x, y, z, n = [int(input()) for num in range(4)]

# possible_coordinates = [[ i, j, k] for i in range(x + 1) 
#                                    for j in range(y + 1)
#                                    for k in range(z + 1)
#                                if (( i + j + k ) != n )] 

#print(possible_coordinates)  

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# ar = []
# p = 0

# for i in range ( x + 1 ) :
#     for j in range( y + 1):
#     	for k in range(z + 1):
#           if i+j+k != n:
#                 ar.append([])
#                 ar[p] = [ i , j, k ]
#                 p+=1
# print(ar) 


#Find the Second Largest Number#


#a_list = [int(input()) for num in range(int(input()))]
# n = input()
# a_list = [int(i) for i in input().split()]

# a = (sorted(list(set(a_list)))[-2])
# print(a) 
#print(sorted(list(set(a_list)))[-2])

# a_list.sort()
# a_set = set(a_list)
# b_list = list(a_set)
# print(b_list[-2])

# n = input()
# a_list = [int(i) for i in input().split()]

# a_set = set(a_list)
# b_list = list(a_set)
# result = sorted(b_list, reverse=True)
# print(result)
# print(result[1])

# Nested Lists#
# Given the names and grades for each student 
# in a Physics class of  students, 
# store them in a nested list and print the name(s) 
#of any student(s) having the second lowest grade.


# students = [[input(), float(input())] for person in range(int(input()))]

# a_dict = dict(sorted(students))
# val = list(a_dict.values())
# mark = sorted(list(set(val)))[1]

# for k, v in a_dict.items():
# 	if v == mark:
# 		print(k)


# For test #
#students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

#a_dict = dict(sorted(students))
#print(a_dict)

#val = list(a_dict.values())
#mark = sorted(list(set(val)))[1]
#print(mark)

# for k, v in a_dict.items():
# 	if v == mark:
# 		print(k)


#book = [['Krishna', [67, 68, 69]], ['Arjun', [70, 98, 63]], ['Malika', [52, 56, 60]]]
#book = [[input(), float(input())] for person in range(int(input()))]

# d_book = dict(book)
# print(d_book)
# marks = d_book['Malika']
# print(marks)
# a, b, c = marks
# res = (a+b+c)//3
# print(res)

#test = input().split()
# students = [[input(), [(input())]] for person in range(int(input()))]

# print(students)


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

