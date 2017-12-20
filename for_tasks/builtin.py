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


def create_data(n):
    data = [x*x for x in range(n)]
    return data

 
@my_timer
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

