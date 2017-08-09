# formatting.py - String Formatting 
# Operations for Dicts, Lists, Numbers, and Dates
# Thanks so much Corey Schafer for the great explanation
# https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g


person = {'name': 'Dasha', 'age': 22}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)

sentence = 'My name is {} and I am {}'.format(person['name'], str(person['age']))
# print(sentence)

sentence = 'My name is {0[name]} and I am {1[age]}'.format(person, person)
# print(sentence)

sentence = 'My name is {0[name]} and I am {0[age]}'.format(person)
# print(sentence)

sentence = 'My name is {name} and I am {age}'.format(**person)
print(sentence)

a_list = ['Andrew', 24]
sentence = 'My name is {0[0]} and I am {0[1]}'.format(a_list)
print(sentence)

tag = 'h1'
text = 'This is headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

class Person():

    def __init__(self, name, age):
    	self.name = name
    	self.age = age

p1 = Person('Bob', 32)    

sentence = 'My name is {0.name} and I am {0.age}'.format(p1)
# print(sentence)

# # Formatting by keywords arg
sentence = 'My name is {name} and I am {age}'.format(name='Kate', age=25)
# print(sentence)

# Format Numbers
for i in range(1, 11):
 	sentence = 'The value is {:02}'.format(i)
 	print(sentence)


pi = 3.14159265359	
sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence) # 3.14

sentence = 'MB is equal to {:,.2f} bytes.'.format(1000**2)
print(sentence) # 1,000,000.00

import datetime
my_date = datetime.datetime(2017, 8, 9, 10, 54, 8)
print(my_date) # 2017-08-09 10:54:08


sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence) # August 09, 2017

# August 09, 2017 fell on a Wednesday and was 221 day of the year
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was {0:%j} day of the year'.format(my_date)
print(sentence)