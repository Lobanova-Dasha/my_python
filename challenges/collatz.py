#! python 3
# collatz.py - Executes The Collatz Sequence, which
# actually works for any integer — sooner or later, 
# using this sequence, you’ll arrive at 1!


def collatz(x) :
	''' If number is even, then collatz() should print number // 2 
	    and return this value. If number is odd,
	    then collatz() should print and return 3 * number + 1. 
	    '''	
	try:
	    if x % 2 == 0:
		    return x // 2
	    elif x % 2 == 1 :
	        return 3 * x + 1
	except TypeError:
	   print('Attention! Type int, not string') 

	         
# This program lets the user type in an integer and keeps calling collatz()
# on that number until the function returns the value 1. 

x = int(input('Type int'))
result = collatz(x)
print(result)
while result != 1 :
    print(collatz(result))
    result = collatz(result)
