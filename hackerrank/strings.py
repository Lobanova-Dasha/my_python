#strings.py

#sWAP cASE#

def swap_case(s):
    return s.swapcase()

s = input()
# # print(swap_case(s))

# #String Split and Join#

def split_and_join(line):

    split_line = line.split(" ")
    join_line = "-".join(split_line)
    print(join_line)

# split_and_join(input())

#What's Your Name?#

def print_full_name(fname, lname):
    print("Hello {} {}! You just delved into python.".format(fname, lname))


# print_full_name(input(), input())   


#Mutations#

def mutate_string(string, posit_char):
	split_posit_char = posit_char.split()
	position = int(split_posit_char[0])
	character = split_posit_char[1]
	string = string[:position] + character + string[position+1:]
	print(string)
    
# mutate_string(input(), input())

# I prefer this way
# def mutate_string(string, position, character):
# 	string = string[:position] + character + string[position+1:]
# 	print(string)
    
#mutate_string(input(), int(input()), input())

# Capitalize! #
def capitalize(string):
	split_str = string.split(" ")
	ar = [i.capitalize() for i in split_str]
	join_line = " ".join(ar)
	print(join_line)
	
# capitalize(input())

# print(" ".join(word.capitalize() for word in input().split(' ')))



# String Formatting #

n = int(input())
width = len(bin(n)) - 2
for x in range(1, (n + 1)):
	print(('%d'%x).rjust(width), 
		   ('%o'%x).rjust(width),
		   ('%X'%x).rjust(width),
		    (str(bin(x))[2:]).rjust(width))
		   






