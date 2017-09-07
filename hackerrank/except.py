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


# № 2 
# You are given a string S. 
# Your task is to find out whether S is a valid regex or not.
import re

for _ in range(int(input())): 

    try:
        print(bool(re.compile(input())))
    
    except:
        print('False')  



              	
