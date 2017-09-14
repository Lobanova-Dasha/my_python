#! python3
# classes.py

import math

# Classes: Dealing with Complex Numbers
# you are given two complex numbers, 
# and you have to print the result of their 
# addition, subtraction, multiplication, division and modulus operations.
# The real and imaginary precision part should be correct up to 
# two decimal places.
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary


    '''addition'''
    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)


    '''subtraction'''
    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)


    '''multiplication'''
    def __mul__(self, no):
        real = self.real*no.real - self.imaginary*no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)


    '''division'''
    def __div__(self, no):
        x = float(no.real**2 + no.imaginary**2)
        y = self * Complex(no.real, -no.imaginary)
        real = y.real/x
        imaginary = y.imaginary/x
        return Complex(real, imaginary)
    

    '''modulus operations'''
    def mod(self):
        real = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(real, 0)


    def __str__(self) :
        return '{0:.2f}{1:+.2f}i'.format(self.r,self.j)    







class Vector:

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def cross(self, other):
        return vector(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)
    
    def mod(self):
        return pow(self.x**2+self.y**2+self.z**2, 0.5)
    
    def __sub__(self, other):
        return vector(self.x-other.x, self.y-other.y, self.z-other.z)
    
    def __add__(self, other):
        return vector(self.x+other.x, self.y+other.y, self.z+other.z)
    
if __name__ == "__main__":
    
    A = vector(*map(float, input().strip().split()))
    B = vector(*map(float, input().strip().split()))
    C = vector(*map(float, input().strip().split()))
    D = vector(*map(float, input().strip().split()))
    AB = B - A
    BC = C - B
    CD = D - C
    X = AB.cross(BC)
    Y = BC.cross(CD)
    print("%.2f"%degrees(acos(X.dot(Y)/X.mod()/Y.mod())))