# coding: utf-8
#! python 2.7
# builtin.py - cheks the complexity(speed) of the operations of searching/inserting/deleting an element
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


def pause(t):
    def wrapper(orig_func):
        def tmp(*args, **kwargs):
            time.sleep(t)
            return orig_func(*args, **kwargs)
        return tmp
    return wrapper



def create_data(n):
    data = [x*x for x in range(n)]
    return data

 
@my_timer
#@pause(4)
def push_elem(structure, elem):
    structure.append(elem)
    return structure


@my_timer
def pop_elem(structure):
    structure.pop()
    return structure


@my_timer    
def unshift(structure, elem, index=0):
    structure.insert(index, elem)
    return structure


@my_timer
def shift(structure, index=0):
    structure.pop(index)
    return structure


@my_timer
def get_elem(structure, index=0):
    return structure[index]


@my_timer
def pop_dict(structure):
    structure.popitem()
    return structure


@my_timer
def del_item(structure, item):
    del structure[item]
    return structure


@my_timer
def update_dict(structure, other):
    structure.update(other)
    return structure      
    

if __name__ == "__main__":
	
    my_list = create_data(10000000)
    my_tuple = tuple(my_list)
    my_dict = {key: val for key, val in enumerate(my_list)}

    # List
    push_elem(my_list, 1234556789)
    pop_elem(my_list)
    unshift(my_list, 1234567, 33)
    shift(my_list)
    get_elem(my_list)
    get_elem(my_list, 6786)
    get_elem(my_list, len(my_list)-1)
    
    # Tuple
    get_elem(my_tuple)
    get_elem(my_tuple, 6786)
    get_elem(my_tuple, len(my_list)-1)

    # Dict
    get_elem(my_dict, 78)
    pop_dict(my_dict)
    del_item(my_dict, 56)
    update_dict(my_dict, my_dict)


# A = set('spam')
# B = set('ham')
# print(A, B)
# print(A & B)
# print(A | B)
# print(A - B)
# print(B - A)
# print(len("a\nb\x1f\000d"))
# print(dict.fromkeys(['a', 'b'], 0))
# print({k:0 for k in 'ab'})
# L = [1,2,3] + [4,5,6]
# print(L, L[:], L[:0], L[-2], L[-2:])
# print(([1,2,3] + [4,5,6])[2:4])
# D = {'x':1, 'y':2, 'z':3}
# D['w'] = 0
# print(D['x'] + D['w'])
# D[(1,2,3)] = 4
# print(D)
# print(list(D.keys()), list(D.values()), (1,2,3) in D)
# print([[]], ["",[],( ),{},None])
# L = [0,1,2,3]
# L[3:1] = ['?']
print(L[3:1])
print(L)

# S = list("spam")
# print(id(S))

# tmp = [x for x in range(10, 20)]
# even = [x for x in tmp if tmp.index(x)%2 == 0]
# iter_ = iter(even)
# print next(iter_)
# print next(iter_)
# print next(iter_)
# print next(iter_)
# print next(iter_)
