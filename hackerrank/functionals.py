#! python3
# functionals.py

# Map and Lambda Function
cube = lambda x: x**3

def fibonacci(n):
    fib = []
    a, b = 0, 1
    for i in range(0, n):
        fib.append(a)
        a, b = b, a + b
    return fib    
  

print(list(map(cube, fibonacci(int(input()))))) 


# Validating Email Addresses With a Filter
import re

def fun(s):
    valid = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    return valid

# import re
# lst = []
# for i in range(int(raw_input())):
#     lst.append(raw_input())
# print sorted(list(filter(lambda x: re.search(r'^[\w\d-]+@[A-Za-z0-9]+\.\w?\w?\w$',x),lst)))    



# def filter_mail(emails):
#     return list(filter(fun, emails))

# if __name__ == '__main__':
#     n = int(input())
#     emails = []
#     for i in range(n):
#         emails.append(input())

# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)    

