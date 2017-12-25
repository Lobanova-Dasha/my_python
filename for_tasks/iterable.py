# coding: utf-8
#! python 2.7
# iterable.py - иду последовательнопо вопросам дока


# Итераторы и итерируемые объекты (сходства, различия, область применения)
# что такое итератор
# уметь написать пример итерируемого объекта и итератора для него

# Iterable object has method __iter__
iter_object = [x*x for x in xrange(1, 10+1)]
#print(dir(iter_object))

# Iterator has methods __iter__and next
my_iter = iter(iter_object)
# print(dir(my_iter))
# print(next(my_iter))

# Функции-генераторы
# что такое генератор
# отличия от обычных функций
# сходства/различия с итераторами
# уметь написать простейший генератор (что-то вроде нечётные числа от a до b)
def my_gen(num):
    seq = [x*x for x in xrange(num+1)]

    for i in seq:
        if i%2 == 1:
            yield i

odd = my_gen(10)
#print(dir(my_gen))
# print(next(odd))
# print(next(odd))
# print(next(odd))
# print(next(odd))
# print(next(odd))
# print(next(odd)) # StopIteration

# or
even_gen = (x**2 for x in xrange(20) if x**2 % 2 == 0)
# print(next(even_gen))
# print(next(even_gen))
# print(next(even_gen))
# print(next(even_gen))
# print(next(even_gen))
# print(next(even_gen))
# print(next(even_gen))


# Синтаксический сахар
# list/dict/set comprehensions
list_comp = [x for x in xrange(100)]
dict_comp = {k:v for k, v in enumerate(xrange(50))}
set_comp = {x for x in [1, 1, 1, 3, 3, 4, 4, 6, 7, 8]}

# generator expressions
gen_exp = (x for x in xrange(100))
#print(type(gen_exp))

