classes.py

import math

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