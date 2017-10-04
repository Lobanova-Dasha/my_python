#! python3
# decorators.py
import time
import logging
from functools import wraps


def my_logger(orig_func):
    
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper
    

def my_timer(orig_func):

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper 


#1 Standardize Mobile Number Using Decorators
def wrapper(orig_func):
    def phone(line):
        orig_func(["+91 "+c[-10:-5]+" "+c[-5:] for c in line])
        return phone
    return wrapper    
        

@my_logger
@my_timer
@wrapper
def sort_phone(line):
    #time.sleep(1)
    print(*sorted(line), sep='\n')

# line = [input() for _ in range(int(input()))]
# sort_phone(line)


#Decorators 2 - Name Directory
def person_lister(orig_func):
    
    @wraps(orig_func)
    def inner(people):
        time.sleep(1)
        return map(orig_func, sorted(people, key=lambda x: x[2]))  
    return inner

@my_logger
@my_timer
@person_lister
def name_format(person):
    return ("Mr. " if person[-1] == "M" else "Ms. ") + person[0] + " " + person[1]    


# people = [input().split() for i in range(int(input()))]
# print(*name_format(people), sep='\n')   