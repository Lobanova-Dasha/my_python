#! python3
# except.py

# № 1 
# Task. You are given two values  a and b. 
# Perform integer division and print a/b.
for i in range(int(input())):
    
    try:
    	a, b = map(int, input().split())
    	print(a//b)

    except ValueError as e:	
        print("Error Code: " + str(e))
    
    except ZeroDivisionError as e:
    	print("Error Code: integer division or modulo by zero")

    finally:
        pass	
