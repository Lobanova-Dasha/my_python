# regex_test.py - examples by Al Sweigart

import re

# Matching Multiple Groups with the Pipe

heroRegex = re.compile(r'Batman|Tina Fey')

mo1 = heroRegex.search('Batman and Tina Fey')
#print(mo1.group()) # Batman

mo2 = heroRegex.search('Tina Fey and Batman')
# print(mo2.group()) # Tina Fey

phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')  

mo1 = phoneNumRegex.search('My number: 416-557-4646')
#print(mo1.group()) # 416-557-4646

mo2 = phoneNumRegex.search('My number: 555-9999')
#print(mo2.group()) # 555-9999


# Matching Zero or More with the Star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group()) # Batman

mo2 = batRegex.search('The Adventures of Batwoman')
#print(mo2.group()) # Batwoman

mo3 = batRegex.search('The Adventures of Batwowowowoman')
#print(mo3.group()) # Batwowowowoman

# Matching One or More with the Plus

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
#print(mo1.group()) # Batwoman

mo2 = batRegex.search('The Adventures of Batman')
#print(mo2 == None) # True

mo3 = batRegex.search('The Adventures of Batwowowowoman')
#print(mo3.group()) # Batwowowowoman

# Matching Specific Repetitions with Curly Brackets
haRegex = re.compile(r'(Ha){3}')

mo1 = haRegex.search('HaHaHa')
#print(mo1.group()) # HaHaHa

mo2 = haRegex.search('Ha')
#print(mo2 == None) # True

# Greedy and Nongreedy Matching
greedyHaRegex = re.compile(r'(Ha){3,5}')

mo1 = greedyHaRegex.search('HaHaHaHa')
#print(mo1.group()) #HaHaHaHa

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')

mo2 = nongreedyHaRegex.search('HaHaHaHa')
#print(mo2.group()) #HaHaHa

# The findall() Method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Mobile: 333-787-8878 Work: 666-333-8888')
#print(mo.group()) # returns a string


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.findall('Mobile: 333-787-8878 Work: 666-333-8888')
#print(mo1) # returns list of strings


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo1 = phoneNumRegex.findall('Mobile: 333-787-8878 Work: 666-333-8888')
#print(mo1) # returns list of tuples

# Character Classes
xmasRegex = re.compile(r'\d+\s\w+')
#print(xmasRegex.findall('''12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 
#	7 swans, 6 geens, 5 rings, 4 birds, 2 doves, 1 partridge'''))


#Making Your Own Character Classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
#print(vowelRegex.findall('RobCop eats baby. BABY FOOD'))

constantRegex = re.compile(r'[^aeiouAEIOU]')
#print(constantRegex.findall('RobCop eats baby. BABY FOOD'))


# The Caret and Dollar Sign Characters
beginsWithHello = re.compile(r'^Hello')

# print(beginsWithHello.search('Hello world!')) # <_sre.SRE_Match object; span=(0, 5), match='Hello'>
# print(beginsWithHello.search('He said hello') == None) # True

endsWithNumber = re.compile(r'\d$')

# print(endsWithNumber.search('Your number is 42')) # <_sre.SRE_Match object; span=(16, 17), match='2'>
# print(endsWithNumber.search('Your number is forty two') == None) # True

whoSelectIsNum = re.compile(r'\d+$')
# print(whoSelectIsNum.search('1234567890')) # <_sre.SRE_Match object; span=(0, 10), match='1234567890'>
# print(whoSelectIsNum.search('12345xyz67890') == None) #False
# print(whoSelectIsNum.search('12 34567890')) # <_sre.SRE_Match object; span=(3, 11), match='34567890'>


#The Wildcard Character
atRegex = re.compile(r'.at')
#print(atRegex.findall('The cat in the hat sat on the flat mat.'))
# ['cat', 'hat', 'sat', 'lat', 'mat']


# Matching Everything with Dot-Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Dasha Last Name: Lobanova')
# print(mo.group(1))
# print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve name> for dinner.>')
# print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo1 = greedyRegex.search('<To serve name> for dinner.>')
# print(mo1.group())


# Matching Newlines with the Dot Character
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('''Serve the public trust. \nProtect the innocent. 
	                        \nUphold the law.''').group())

NewlineRegex = re.compile('.*', re.DOTALL)
print(NewlineRegex.search('''Serve the public trust. \nProtect the innocent.
                          \nUphold the law.''').group())