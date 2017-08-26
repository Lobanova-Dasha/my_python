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

alpha = list(filter((lambda x: x.isalpha()), line))

lower = list(filter((lambda x: x.islower()), alpha))
lower.sort()

upper = list(filter((lambda x: x.isupper()), alpha))
upper.sort()

digits = list(filter((lambda x: x.isdigit()), line))
digits = list(map(int, digits))

odd = list(filter((lambda x: x%2==1), digits))
odd.sort()

even = list(filter((lambda x: x%2==0), digits))
even.sort()

new_digit = list(map(str, odd + even))

my_seq = lower + upper + new_digit


print(reduce((lambda x, y: x + y), my_seq))




