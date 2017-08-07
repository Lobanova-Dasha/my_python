#! python3
# learningOOP.py - Consists oop challenges by Bill Lubanovic

# 6.1. Create an empty class and an instance of it
# print them
# they are the same?

class Thing:
	pass

example = Thing() # print(Thing) # <class '__main__.Thing'>
                  # print(example) # <__main__.Thing object at 0x038FC170>

# 6.2. Make a new class called Thing2 
# and assign the value 'abc' to a class attribute calledletters. 
# Print letters 

class Thing2:
    letters = 'abc'

#print(Thing2.letters)

# 6.3. Make yet another class called, of course, Thing3. 
# This time, assign the value 'xyz'to an instance (object) attribute 
# called letters. Print letters. 
# Do you need to make an object from the class to do this?

class Thing3:
    def __init__(self):
    	self.letters = 'xyz'

smth = Thing3()
#print(smth.letters)   	

# 6.4. Make a class called Element, 
# with instance attributes name, symbol, and number.
# Create an object of this class with the values 'Hydrogen', 'H', and 1.
     
class Element():
	def __init__(self, name, symbol, number):
	    self.name = name
	    self.symbol = symbol
	    self.number = number
	def dump(self):
	    print('name = %s, symbol = %s, number = %s' %
	    	(self.name, self.symbol, self.number))    

element = Element('Hydrogen', 'H', 1)
#print(element.name, element.symbol, element.number)
#hydrogen.dump()
#print(hydrogen)

# 6.5. Make a dictionary with these 
#keys and values: 'name': 'Hydrogen', 'symbol':'H', 'number': 1. 
#Then, create an object called hydrogen from class Element using this
# dictionary
el_dict = {'name' : 'Hydrogen', 'symbol' : ' H', 'number' : 1}

hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
hydrogen.name

# Using of namedtuple
from collections import namedtuple
hydrogen = Element(**el_dict)

# 6.8. Modify Element to make the attributes name, symbol, and number private. 
# Define a getter property for each to return its value.
class Element():
	def __init__(self, name, symbol, number):
	    self.__name = name
	    self.__symbol = symbol
	    self.__number = number
	@property
	def name(self):
		return self.__name
	@property	
	def symbol(self):
	    return self.__symbol
	@property    
	def number(self):
	    return self.__number  
	
hydrogen = Element('Hydrogen', 'H', 1)
# print(hydrogen.name)
# print(hydrogen.symbol)
# print(hydrogen.number)	

# 6.9 Define three classes: Bear, Rabbit, and Octothorpe. 
# For each, define only one method: eats(). 
# This should return 'berries' (Bear), 'clover' (Rabbit), and 'campers'
# (Octothorpe). Create one object from each and print what it eats.
class Bear():
	def eats(self):
		print('berries')

class Rabbit():	
    def eats(self):
    	return 'clover' # if return, use print for print

class Octotohorpe():
    def eats(self):
        print('campers')

bear = Bear()
rabbit = Rabbit()
octotohorpe = Octotohorpe()

# bear.eats()
# print(rabbit.eats())
# octotohorpe.eats()  

# 6.10. Define these classes: Laser, Claw, and SmartPhone. 
# Each has only one method:does(). 
# This returns 'disintegrate' (Laser), 'crush' (Claw), 
# or 'ring' (SmartPhone). Then, define the class Robot 
# that has one instance (object) of each of these. Define a does() 
# method for the Robot that prints what its component objects do.
class Laser():
	def does(self):
		return 'disintergrate'

class Claw():
	def does(self):
		return 'crush'

class SmartPhone():
    def does(self):
    	return 'ring'

laser = Laser()
claw = Claw()
smart_ph = SmartPhone()
   	
class Robot(Laser, Claw, SmartPhone):
	def does(self):
		return ''' I have many attachments:
	My laser, to %s.
	My claw, to %s.
	My smatrhone, to %s.''' % (
		laser.does(), 
		claw.does(), 
		smart_ph.does()) 

robbie = Robot()
#print(robbie.does())	

    			
