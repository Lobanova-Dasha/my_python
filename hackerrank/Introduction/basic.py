basic.py

def main():
    n = int(input())
    if n % 2 == 1:
        print('Weird')
    elif n % 2 == 0 and (2 <= n <= 5):
        print('Not Weird')
    elif n % 2 == 0 and (6 <= n <= 20):  
        print('Weird')
    elif n % 2 == 0 and n > 20:
        print('Not Weird')
    
if __name__ == '__main__':
    main()
   
  
    elif year % 100 == 0:
        return True


def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False  

year = int(input()) 
print(is_leap(year))       
        

# Print Function
# from __future__ import print_function
# import sys, os, time

# n = int(input())

# for x in range(1,(n+1)):
#     print(x, sep=' ', end='')  
#     time.sleep(1)


print(*range(1, int(input()) + 1), sep="")  

# list(map(lambda x:print(x + 1, end=''), range(int(input()))))