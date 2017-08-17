#strings.py

#sWAP cASE#

def swap_case(s):
    return s.swapcase()

s = input()
# print(swap_case(s))

#String Split and Join#

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
    

mutate_string(input(), input())

# I prefer this way
# def mutate_string(string, position, character):
# 	string = string[:position] + character + string[position+1:]
# 	print(string)
    

#mutate_string(input(), int(input()), input())







