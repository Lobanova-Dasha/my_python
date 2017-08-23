#strings.py


#sWAP cASE#
def swap_case(s):
    return s.swapcase()


s = input()
print(swap_case(s))


#String Split and Join#
def split_and_join(line):
    split_line = line.split(" ")
    join_line = "-".join(split_line)
    print(join_line)


split_and_join(input())


# #What's Your Name?#
def print_full_name(fname, lname):
    print("Hello {} {}! You just delved into python.".format(fname, lname))


print_full_name(input(), input())   


#Mutations#

def mutate_string(string, posit_char):
	split_posit_char = posit_char.split()
	position = int(split_posit_char[0])
	character = split_posit_char[1]
	string = string[:position] + character + string[position+1:]
	print(string)
    
mutate_string(input(), input())

# I prefer this way
def mutate_string(string, position, character):
	string = string[:position] + character + string[position+1:]
	print(string)
    

mutate_string(input(), int(input()), input())


# Capitalize! #
def capitalize(string):
	split_str = string.split(" ")
	ar = [i.capitalize() for i in split_str]
	join_line = " ".join(ar)
	print(join_line)
	
capitalize(input())

# Another way, the same result
print(" ".join(word.capitalize() for word in input().split(' ')))


# String Formatting #
n = int(input())
width = len(bin(n)) - 2

for x in range(1, (n + 1)):
	print(('%d'%x).rjust(width), 
		  ('%o'%x).rjust(width),
		  ('%X'%x).rjust(width),
          (str(bin(x))[2:]).rjust(width))

		   
#Find a string#
import re

a = input()
b = input()

match = re.findall('(?='+b+')',a)
print(len(match))


#String Validators#
str = input()

print(any(c.isalnum() for c in str))
print(any(c.isalpha() for c in str))
print(any(c.isdigit() for c in str))
print(any(c.islower() for c in str))
print(any(c.isupper() for c in str))

#Text Wrap#
s = input().strip()
w = int(input())
for i in range(0, len(s)+1, w):
    print(s[i:w+i])

# Using textwrap
import textwrap

s = input()
w = int(input())
print(textwrap.fill(s,w))

# Text Alignment

# The Minion Game 

# Merge the Tools! 
line = input()
num = int(input())
num_subsegments = int(len(line) / num)

# for index in range(num_subsegments):
    
#     # Subsegment string by by ordered unique values
#     result = sorted(list(set(list(line[index*num:(index+1)*num]))))
   
#     #Print final converted string
#     print("".join(result))


for index in range(num_subsegments):
    # Subsegment string
    t = line[index*num : (index + 1)*num]
    
    # Subsequence string having distinct characters
    u = ""
    
    # If a character is not already in 'u', append
    for c in t:
        if c not in u:
            u += c

    # Print final converted string
    print(u)





