#! python3
# decorators.py


#Standardize Mobile Number Using Decorators
# line = [input() for _ in range(int(input()))]

# def wrapper(orig_func):
#     def phone(line):
#         orig_func(["+91 "+c[-10:-5]+" "+c[-5:] for c in line])
#     return phone

# @wrapper
# def sort_phone(line):
#     print(*sorted(line), sep='\n')

# sort_phone(line)


def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: x[2]))  
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[-1] == "M" else "Ms. ") + person[0] + " " + person[1]    


people = [input().split() for i in range(int(input()))]
print(*name_format(people), sep='\n')    