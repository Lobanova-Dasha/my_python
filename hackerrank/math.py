# math.py

# Mod Divmod
n1, n2 = int(input()),int(input())

d = divmod(n1, n2)
print(d[0])
print(d[1])
print(d)


# Integers Come In All Sizes
def sum_of_mult(a, b, c, d):
	print(a**b + c**d)


a, b, c, d = int(input()), int(input()), int(input()), int(input())
sum_of_mult(a, b, c, d)


# Power - Mod Power
a, b, c = int(input()), int(input()), int(input())

print(pow(a,b))
print(pow(a,b,c))


# Triangle Quest
for i in range(1,int(input())): 
    print(str(i)*i) 
    #print((10**(i)//9)*i)        


# Find Angle MBC
import math
AB = float(input())
BC = float(input())

print(str(int(round(math.degrees(math.atan2(AB, BC)))))+'°')  


# Triangle Quest 2
for x in range(1,int(input())+1):
    print(((10**x - 1)//9)**2)
     

# 10**x  10**x - 1 (10**x - 1)//9) (10**x - 1)//9)**2
# 10       9       1                1
# 100      99      11               121
# 1000     999     111              12321
# 10000    9999    1111             1234321
# 100000   99999   11111            123454321  


# Polar Coordinates
from cmath import polar

polar = polar(complex(input()))

print(polar[0])
print(polar[1])

