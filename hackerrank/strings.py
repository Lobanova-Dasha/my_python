#strings.py

#sWAP cASE#

# def swap_case(s):
#     return s.swapcase()

# s = input()
# # # print(swap_case(s))

# # #String Split and Join#

# def split_and_join(line):

#     split_line = line.split(" ")
#     join_line = "-".join(split_line)
#     print(join_line)

# # split_and_join(input())

# #What's Your Name?#

# def print_full_name(fname, lname):
#     print("Hello {} {}! You just delved into python.".format(fname, lname))


# # print_full_name(input(), input())   


# #Mutations#

# def mutate_string(string, posit_char):
# 	split_posit_char = posit_char.split()
# 	position = int(split_posit_char[0])
# 	character = split_posit_char[1]
# 	string = string[:position] + character + string[position+1:]
# 	print(string)
    
# # mutate_string(input(), input())

# # I prefer this way
# # def mutate_string(string, position, character):
# # 	string = string[:position] + character + string[position+1:]
# # 	print(string)
    
# #mutate_string(input(), int(input()), input())

# # Capitalize! #
# def capitalize(string):
# 	split_str = string.split(" ")
# 	ar = [i.capitalize() for i in split_str]
# 	join_line = " ".join(ar)
# 	print(join_line)
	
# # capitalize(input())

# # print(" ".join(word.capitalize() for word in input().split(' ')))



# # String Formatting #

# n = int(input())
# width = len(bin(n)) - 2
# for x in range(1, (n + 1)):
# 	print(('%d'%x).rjust(width), 
# 		   ('%o'%x).rjust(width),
# 		   ('%X'%x).rjust(width),
# 		    (str(bin(x))[2:]).rjust(width))
		   
#Find a string#
# import re

# a = input()
# b = input()
# match = re.findall('(?='+b+')',a)
# print(len(match))

#String Validators#
# str = input()
# print(any(c.isalnum() for c in str))
# print(any(c.isalpha() for c in str))
# print(any(c.isdigit() for c in str))
# print(any(c.islower() for c in str))
# print(any(c.isupper() for c in str))

#Text Wrap#

# s = input().strip()
# w = int(input())
# for i in range(0, len(s)+1, w):
#     print(s[i:w+i])

# import textwrap
# def 
# s = input()
# w = int(input())
# print(textwrap.fill(s,w))





# n = int(input())
# for i in range(n):
#     s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
#     print((s+s[::-1][1:]).center(n*4-3, '-'))

# for i in range(n-1):
#     s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
#     print((s+s[::-1][1:]).center(n*4-3, '-'))



# import math

# c='♥'
# width = 40

# print ((c*2).center(width//2)*2)

# for i in range(1,width//10+1):
#     print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
#            (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)

# for i in range(width//4,0,-1):
#     print ((c*i*4).center(width))
# print ((c*2).center(width))

# Replace all ______ with rjust, ljust or center.

