# Comprehensions Python

## List Comprehensions ##
 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' ib nums
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

my_list = [n for n in nums]	
print(my_list)

#I want 'n*n' for each n in nums
# my_list = []
# for n in nums:
# 	my_list.append(n*n)
# print(my_list)	

my_list = [n*n for n in nums]
print(my_list)

# Using a map + lambda
# my_list = map(lambda n: n*n, nums)
# print(my_list)


# I want 'n' for each n in nums if n is even
# my_list = []
# for n in nums:
# 	if n % 2 == 0:
# 		my_list.append(n)
# print(my_list)	

my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# Using a filter + lambda
# my_list = filter(lambda n: n%2 ==0, nums)
# print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' for each number in '0123'
# my_list = []
# for letter in 'abcd':
# 	for num in range(4):
# 		my_list.append((letter, num))
# print(my_list)		

my_list = [(letter, num) for letter in 'abcd' for num in (range(4))]
print(my_list)



## Dictionary Comprehensions ##
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman','Spiderman', 'Wolverine', 'Deadpool']

# print(list(zip(names, heros)))

# I want a dict{'name: 'hero} for each name, hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
# 	my_dict[name] = hero
# print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

# if name not equal to Peter
# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}

## Set Comprehensions ##

nums = [1, 4, 8, 4, 0, 4, 5, 6, 4, 6, 5, 9, 0, 3, 7, 6, 4, 9, 3]

# my_set = set()
# for n in nums:
# 	my_set.add(n)
# print(my_set)

# my_set ={n for n in nums}
# print(my_set)

## Generator Expressions ##	
# I want to yield 'n*n' foe each n in nums

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def gen_func(nums):
#     for n in nums:
# 	    yield n*n

# my_gen = gen_func(nums)	

my_gen = (n*n for n in nums)
for i in my_gen:
	print(i)











