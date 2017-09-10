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


#7 Validating Roman Numerals
thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'

print(bool(re.match(thousand + hundred+ten+digit +'$', input())))

# I'm shocked. Python has Roman module
from roman import fromRoman

try:
    if 0<fromRoman(input())<4000:
        print(True)
    else:
  
        print(False)
except:
    print(False)


#8 Validating phone numbers
for i in range(int(input())):
    if re.match(r'[789]\d{9}$', input()):   
        print('YES')  
    else:  
        print('NO')  


#9 Hex Color Code
for i in range(int(input())):
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    
    if matches:
        print(*matches, sep='\n')        


#10 Validating and Parsing Email Addresses
import email.utils

for _ in range(int(input())):
    t = email.utils.parseaddr(input())

    if bool(re.match('[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$',t[1])):
        print(email.utils.formataddr(t))


#11 HTML Parser - Part 1
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):        
        print('Start :',tag)
        for elem in attrs:
            print('->',elem[0],'>',elem[1])
            
    def handle_endtag(self, tag):
        print('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print('Empty :',tag)
        for elem in attrs:
            print('->',elem[0],'>',elem[1])
            
MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))


#12
#from html.parser import HTMLParser
class CustomHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
        number_of_line = len(data.split('\n'))
        if number_of_line>1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

parser = CustomHTMLParser()

n = int(input())

html_string = ''
for i in range(n):
    html_string += input().rstrip()+'\n'
    
parser.feed(html_string)
parser.close()


#13 Detect HTML Tags, Attributes and Attribute Values
#from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
        
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()


#14 Validating UID

for _ in range(int(input())):
    
    uid = ''.join(sorted(input()))
    
    try:
        assert re.search(r'[A-Z]{2}', uid)
        assert re.search(r'\d\d\d', uid)
        assert not re.search(r'[^a-zA-Z0-9]', uid)
        assert not re.search(r'(.)\1', uid)
        assert len(uid) == 10
    except:
        print('Invalid')
    else:
        print('Valid')


#15 Validating Credit Card Numbers
valid = r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$"
invalid = r"([\d])\1\1\1"

for _ in range(int(input())):
    s = input()

    if re.match(valid, s) and not re.search(invalid, s.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")    
