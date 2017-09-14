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


# Class 2 - Find the Torsional Angle
# Task. You are given four points  A,B,C and D  in a 
# 3-dimensional Cartesian coordinate system. 
# You are required to print the angle between 
# the plane made by the points A,B,C and B,C,D in degrees(not radians). 
# Let the angle be PHI. 

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        x = self.x-no.x
        y = self.y-no.y
        z = self.z-no.z
        return Points(x, y, z)

    def dot(self, no):
        x = self.x*no.x
        y = self.y*no.y
        z = self.z*no.z
        return x+y+z

    def cross(self, no):
        x = self.y*no.z - self.z*no.y
        y = self.z*no.x - self.x*no.z
        z = self.x*no.y - self.y*no.x
        return Points(x, y, z)

    def absolute(self):
        return pow((self.x**2 + self.y**2 + self.z**2), 0.5)


if __name__ == '__main__':
    points = []
    for i in range(4):
        a = map(float, input().split())
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b-a).cross(c-b)
    y = (c-b).cross(d-c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print('{0:.2f}'.format(math.degrees(angle)))                
        
