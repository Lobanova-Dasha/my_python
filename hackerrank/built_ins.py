# built-ins.py

# Zipped! 
n = list(map(int, input().split()))

sheet = []
for i in range(n[1]):
    scores = list(map(float, input().split()))
    sheet.append(scores) 

new_sheet = list(zip(*sheet))

avr = list(map(sum, new_sheet))
for x in avr:
    print(float(x/n[1]))


# Input()
x, k = map(int, input().split())
print(eval(input()) == k)


# Python Evaluation
eval(input())


# Sort Data
n, m = map(int, input().split()) # actually, 'm' is useless argument
rows = [input() for i in range(n)]
indx = int(input()) # The table must be sorted by the row's index 

for row in sorted(rows, key=lambda row: int(row.split()[indx])):
    print(row)


# Any or All
useless_arg = int(input())
num_lst = input().split()

print(all([int(num)>=0 for num in num_lst]) 
	  and 
      any([num == num[::-1] for num in num_lst]))


# ginortS
from functools import reduce

line = input()

# Extract alpha values from line
alpha = list(filter((lambda x: x.isalpha()), line))

# Extract lowercase letters from alpha and sort them
lower = list(filter((lambda x: x.islower()), alpha))
lower.sort()

# Extract uppercase letters from alpha and sort them
upper = list(filter((lambda x: x.isupper()), alpha))
upper.sort()

# Extract digital values from line
digits = list(filter((lambda x: x.isdigit()), line))
digits = list(map(int, digits))

# Extract odd from digits and sort them
odd = list(filter((lambda x: x%2==1), digits))
odd.sort()

# Extract even from digits and sort them
even = list(filter((lambda x: x%2==0), digits))
even.sort()

# Convert digital sequence to string
new_digit = list(map(str, odd + even))

# Using join, for or while anywhere will result in a score of 0 
my_seq = lower + upper + new_digit

# Get ordered line
print(reduce((lambda x, y: x + y), my_seq))
