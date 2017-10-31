# generator.py
import time
from functools import wraps



# def timer(func, *args, ** kwargs):
#     start = time.clock()
#     for i in repslist:
#         result = func(*args, **kwargs)
#     elapsed = time.clock() - start
#     return(elapsed, ret)    

def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in {} sec'.format(orig_func.__name__, t2))
        return result
 
repslist = range(1000)

@my_timer 
def for_loop():
    res = []
    for x in repslist:
        res.append(abs(x))

def list_comp():
    return [abs(x) for x in repslist]


# print(sys.version)

# for test in (for_loop, list_comp):
#     elapsed, result = timer.timer(test)
#     print('-' * 33)
#     print('{}: {} => [{}....{}]'.format(test.__name__, elapsed, result[0], result[-1]))        



# def square_numbers(nums):
# 	result = []
# 	for i in nums:
# 		result.append(i*i)
# 	return result


#def square_numbers(nums):
# 	for i in nums:
# 		yield i*i
			
# # my_nums = square_numbers([1, 2, 3, 4, 5]) 
# # my_nums = [x*x for x in [1, 2, 3, 4, 5]]
# # print(my_nums) # [1, 4, 9, 16, 25]

# my_nums = (x*x for x in range(1, 6))
# print(my_nums) # <generator object <genexpr> at 0x0000018E0AD98AF0>
# print(list(my_nums)) # [1, 4, 9, 16, 25]

# for num in my_nums:
#     print(num)
