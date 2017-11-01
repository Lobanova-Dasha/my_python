# generator.py
import time
from functools import wraps

def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper 
 
repslist = range(10000000)

@my_timer 
def for_loop():
    res = []
    for x in repslist:
        res.append(x+10)

@my_timer 
def list_comp():
    return [x+10 for x in repslist]

@my_timer
def map_call():
    return list(map((lambda x: x + 10), repslist))

@my_timer
def gen_expr():
    return list(x+10 for  x in repslist)       

# for_loop()
# list_comp()
# map_call()
# gen_expr()


def square_numbers(nums):
	result = []
	for i in nums:
		result.append(i*i)
	return result


def square_numbers(nums):
	for i in nums:
		yield i*i
			
my_nums = square_numbers([1, 2, 3, 4, 5]) 
my_nums = [x*x for x in [1, 2, 3, 4, 5]]
# print(my_nums) # [1, 4, 9, 16, 25]

my_nums = (x*x for x in range(1, 6))
print(my_nums) # <generator object <genexpr> at 0x0000018E0AD98AF0>
print(list(my_nums)) # [1, 4, 9, 16, 25]

# for num in my_nums:
#     print(num)

     