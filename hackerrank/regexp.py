#! python3
# regexp.py

import re

#1 Introduction to Regex Module

for i in range(int(input())):
    print(bool(re.search(r"^[+-]?\d*\.\d+$", input().strip())))


#2 Re.split()

for i in re.split(r'[.,]', input()):
    if i.isdigit():
        print(i)    

#3 Group(), Groups() & Groupdict()
m = re.search(r'([A-Za-z0-9])\1+', input())

if m:
    print(m.group(1))
else:
    print(-1)


#4 Re.findall() & Re.finditer() 
v = "aeiou" # Vowels 
c = "qwrtypsdfghjklzxcvbnm" # Consonants

m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))


#5 Re.start() & Re.end()
a_str, substr = input(), input()
matches = list(re.finditer(r'(?={})'.format(substr), a_str))

if matches:
    print('\n'.join(str((match.start(), match.start() + len(substr) - 1)) 
          for match in matches))
else:
    print('(-1, -1)')


#6 Regex Substitution
for _ in range(int(input())):
    line = input()
    
    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")
    
    print(line)