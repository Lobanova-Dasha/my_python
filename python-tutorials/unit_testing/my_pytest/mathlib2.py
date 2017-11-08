#mathlib2.py
import math
from datetime import datetime
import sys


def calc_square(num):
    return num*num

    
def calc_total(a, b):
    return a+b

def calc_multiply(a, b):
    return a*b

def my_function(x, y):
    if x not in range(0, 9) or y not in range(0, 9):
        raise ValueError

    return math.sqrt(x**2 + y**2)
    

def are_we_in_future():
    if datetime.now().year >= 2100:
        return True
    else:
        return False
       
# print(are_we_in_future()) 

class AdderWithSaturation(object):
    def __init__(self):
        self.value = 0

    def add(self, value_to_add):
        tmp = self.value + value_to_add
        if tmp <= 10:
             self.value = tmp
        else:
             self.value = 10

val = AdderWithSaturation()

val.add(2)
val.add(9)

print(val.value)            