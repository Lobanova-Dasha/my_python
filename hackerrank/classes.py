classes.py

# Day 4: Class vs. Instance 
# Task. Write a Person class with an instance variable, age, 
# and a constructor that takes an integer, initialAge, as a parameter. 
# The constructor must assign initialAge to age after confirming 
# the argument passed as initialAge is not negative; 
# if a negative argument is passed as initialAge, 
# the constructor should set age to 0  
# and print Age is not valid, setting age to 0..


class Person:

    def __init__(self,initialAge):
        
        self.age = 0

        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge


    def amIOld(self):
        
        if age < 13:
            print('You are young.')
        elif 13<=age<18:
            print('You are a teenager.')
        else:
            print('You are old.')   
        

    def yearPasses(self):
        # Increment the age of the person in here global age
        age += 1 


t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")         