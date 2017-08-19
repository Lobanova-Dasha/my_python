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