#! python3
# basic_dt.py

#Tuples#
#Type n space-separated integers:

print(hash(tuple([int(i) for i in input().split()])))

# print(hash(tuple([1, 2, 3])))

#List Comprehensions#

# There are three integers X, Y, Z  
# that are representing the dimensions of a cuboid along with an integer 
# I want to create a list of all possible coordinates 
# given by (i, j, k)  on a 3D grid 
# where the sum of i+j+k is not equal to N.

x = int(input())
y = int(input())
z = int(input())
n = int(input())

possible_coordinates = [[ i, j, k] for i in range(x + 1) 
                                   for j in range(y + 1)
                                   for k in range(z + 1)
                               if (( i + j + k ) != n )] 

print(possible_coordinates)  

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

