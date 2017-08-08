#sorting.py
# Thanks so much Corey Schafer for the great explain
# https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g

# Sorting Lists
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# s_li = sorted(li) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# s_li = li.sort() # None
s_li = sorted(li, reverse=True) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

print('Sorted Variable:\t', s_li)

li.sort()
print('Original Variable:\t', li)

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li) # li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key = abs) # [1, 2, 3, -4, -5, -6]


# Sorting Tuples
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Tuple\t', s_tup)

# Sorting Dicts
di = {'name': 'Dasha', 'job': 'programming', 'age': None, 'dog': 'Lebowski'}
s_di = sorted(di) # ['age', 'dog', 'job', 'name']
print('Soreted dict is just sorted keys\t', s_di)

# Sorting Objects

class Employee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
	    return '({},{},${})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

def e_sort(emp):
	return emp.name # I can use other keys for sorting too

s_employees = sorted(employees, key=e_sort)
print(s_employees) #[(Carl,37,$70000), (John,43,$90000), (Sarah,29,$80000)]

# Using lambda
s_employees = sorted(employees, key=lambda e: e.name) #the same result

# Or attrgetter
s_employees = sorted(employees, key=attrgetter('age'))
