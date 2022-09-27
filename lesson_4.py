def person(age, last_name, name):
    return f'Hello, my name is {name} {last_name}, Iam {age} years old'

print(person(30, 'Smith', "Jane"))

# #------------

def person(age, last_name='Smith', name='Jane'):
    return f'Hello, my name is {name} {last_name}, Iam {age} years old'

print(person(30))

# # #------------

def person(age, last_name='Smith', name='Jane'):
    return f'Hello, my name is {name} {last_name}, Iam {age} years old'

print(person(30, name='Alice'))

# #-----------

def person(age, last_name='Smith', name='Jane'):
    return f'Hello, my name is {name} {last_name}, Iam {age} years old'

print(person(name='Alice', age=17))

# # #-----------

min_arg = min(5,3,7,5,9)
print(min_arg)

# #-----------

def pattern(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1

print(pattern(char2='*', length=9))

# # #-----------

x = 15
y = 78

def sum_it(x,y):
    print(f'Locals:{locals()}')
    return x + y

print(f'Inside the function: {sum_it(5,8)}')
print(f'Outside the function: {x + y}')
print(f'Globals: {globals()}')

# # #-----------

print((lambda x, y: x*y)(5,2))
mult = lambda x,y: x*y
print(mult(5,2))

# #-----------
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100, True, 'lol']
def take_odd(num):
    if isinstance(num, int) and num % 2:
        return True
    return False
print(list(filter(take_odd, list_1)))

# # #------------
list_3 = [1,2,5,8,7,45,600]
print(list(filter(take_odd, list_3)))

# #-----------
print(list(filter(lambda x: x%2, list_3)))

# #-----------
new_l = []
for item in list_1:
    if isinstance(item, str) and 'a' in item:
        new_l.append(item)
print(new_l)


filtered = list(filter(lambda x: isinstance(x, str), list_1))
print(list(filter(lambda x: 'a' in x, filtered)))

# # #------------
#from functools import reduce
import functools
res = functools.reduce(lambda x,y: x+y, [1,5,8,11,13])
print(res)


import my_module_lesson_4
print(my_module_lesson_4.sum_it(5,8))
print(my_module_lesson_4.prod(2,5))

# # #------------
from my_module_lesson_4 import *
def tests():
    assert sum_it(5,8) == 13
    assert prod(10, 6) == 60
    assert div(10, 0) == 'ZERO DIVISION'
    assert sub(8, 5) == 3
tests()

# #------------

import math
arr = [1,2,3,4,5,10,25]
new_arr = math.prod(arr)
print(new_arr)

import datetime
birth_year = 1980
current_date = datetime.date.today()
current_age = datetime.date.today().year - birth_year
current_month =datetime.date.today().month
print(current_date)
print(current_age)
print(current_month)


def sum_it(**kwargs):
    return sum(kwargs.values())
print(sum_it(num1=4, num2=5, num3=10)) #ИМЕНОВАННЫЕ АРГУМЕНТЫ  КАК СЛОВАРЬ


def sum_it_again(*args):
    return sum(args)
print(sum_it_again(2,5,4,7,8,5,4,3))

list_2 = [1,2,3,4,5]
print(list(map(lambda x: x*x,list_2)))

#HOMEWORK
'''
4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
(с помощью кортежа):
     периметр квадрата, площадь квадрата и диагональ квадрата.
'''
import math



def square(arg):

    perimetr = arg * 4
    ploshad = (arg ** arg)
    diagonal = arg * math.sqrt(2)
    return perimetr, ploshad, diagonal
print(square(5))
import functools

'''
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и
# выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
# 	'''
def my_func(**kwargs):
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))
my_func(name='John', last_name='Smith')


# '''
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21]
# создайте новый список, содержащий только
#      положительные числа
#      '''
my_list = [20, -3, 15, 2, -1, -21]
my_new_list = list(filter(lambda x: x > 0, my_list))
print(my_new_list)

'''
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# '''
import functools
my_new_list = functools.reduce(lambda x, y: x * y, my_new_list)
print(my_new_list)

# '''
# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции,
# выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
# '''
import my_module_lesson_4
print(my_module_lesson_4.sub(4,3))
print(my_module_lesson_4.prod(4,3))
print(my_module_lesson_4.div(4,3))
print(my_module_lesson_4.sum_it(4,3))

