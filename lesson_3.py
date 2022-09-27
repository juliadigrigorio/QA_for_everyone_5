l = []
print(l)


l = [1, 'string', 12.3, 'Hello', 25]
print(l)

#------------

sentence = 'What a wonderful day'
my_list = list(sentence)
print(my_list)


my_list = sentence.split(' ')
print(my_list)
print(my_list[-1])

'''
МЕТОДЫ РАБОТЫ СО СПИСКАМИ:
.append()
.insert()
.index()
.clear()
.remove()
.reverse()
.count()
sum()
min()
max()
'''

m = [8, 7, 5, 10]
print(m)
print(id(m))
m[0] = 0
print(m)
print(id(m))

#------------

m1 = [25, 80]
m.append(m1)
print(m)
print(m[-1][1])

#------------

add = 'extra'
m.append(add)
m1.extend(add)
print(m)
print(m1)

#------------

nums = [2,3,1,5,6,4,0]
print(f'Initial list: {nums}')
print(id(nums))
print('SORTED()')
print(f'New sorted list: {sorted(nums)}')
print(id(sorted(nums)))
print('.SORT()')
print(f'New sorted list: {nums.sort()}') # None
print(f'Initial list after sorting: {nums}')
print(id(nums))
print(nums.reverse())
print(nums)
print(id(nums))

#------------

str1 = 'hgjfkdlhg456'
print(sorted(str1))
print(sorted(str1, reverse=True))

#------------

letters = ['a', 'b', 'c', 'd', 'e', 'f' ]
print(letters[0:-1:2])
print(letters[-3])
print(letters[::-1])
print(letters[1:-1])

#------------

#LIST COMPREHENTION
l = [1,2,3,4,5]
new_l = []
for x in l:
    if x % 2:
        new_l.append(x*x)
print(new_l)



new_l = [x*x for x in l if x % 2]
print(new_l)


#TUPLES

my_tuple = 1,2,3
print(my_tuple)

#------------

my2_tuple = (1, True, 'name', None, 'name', 'name', 25)
print(my2_tuple)

#------------

my3_tuple = 'Mark',
print(my3_tuple)

#------------

my4_tuple = ('Mark',)
print(my4_tuple)

my5_tuple_string = ('Mark')
print(my5_tuple_string)

#------------

letters = ('apple', 'banana', 'cat')
a,b,c = letters
print(a)
print(b)
print(c)

#------------

letters = list(letters)
letters[0] = 'ananas'
print(letters)
print(tuple(letters))

#------------

my_tuple = (1, True, 'name', None, 'name', 'name', 25)
print(my_tuple.index('name'))
print(my_tuple.count('name'))

#------------

my_tuple = (1, True, 'name', None, 'name', 'name', 25)
result = tuple(filter(lambda x: isinstance(x, int), my_tuple))
print(result)
print(f'Sum is: {sum(result)}')
print(f'Max is: {max(result)}')
print(f'Min is: {min(result)}')
print(f'Length is: {len(result)}')
print(f'Length is: {len(my_tuple)}')

#------------

my_tuple = (1, True, 'name', None, 'name', 'name', 25)
for (index, item) in enumerate(my_tuple):
    print(index,item)

#------------

i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1

#------------


letters = ('apple', ['ananas', 'mango'], 'melon')
letters[1][0] = 'cherry'
print(letters)

#------------

a = 5
b = 10
a,b = b,a
print(f'a = {a}')
print(f'b = {b}')

#------------

def sum_it(*args):
    total = 0
    for num in args:
        total = total + num
    return total
print(sum_it(4,5,10,6,20))

#------------

def func(*args):
    l = []
    for item in args:
        l.append(item * item)
    return l
print(func(2,5,6,8,10))

#------------

my_dict= {
    'name': 'Anna',
    'last_name': 'Pavlova',
    'age': 30,
    'department': 'IT'
}

print(my_dict)
print(id(my_dict))
print(my_dict['name'])
my_dict['last_name'] = 'Smirnova'
print(my_dict)
print(id(my_dict))
print(len(my_dict))
my_dict['Salary'] = 5000
print(my_dict)

'''
МЕТОДЫ РАБОТЫ СО СЛОВАРЯМИ
.keys()
.items()
.get()
.clear()
.copy()
len()
type()
min()
max()
'''
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.pop('name'))
print(my_dict.get('name', 'Not found'))
print(my_dict.get('age', 'how old'))

#------------

print(set([1,8,2,1,5,8,9]))

set1 = {1,2,3, 'one', 'two'}
set2 = {1,2,3,'one', 'ten', 100, 525}
set3 = {1,2,3}

print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set2.intersection(set1))
print(set1.difference(set2))
print(set1)
print(set1.remove(1))
print(set1)
print(set1.add(8))
print(set1)

#------------

fs = frozenset({1,2,3}) #заморозить чтоб ни добавить ни удалить
print(fs)

#------------


#HOMEWORK

#3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

my_list = ['a', 'b', [1, 2, 3], 'd']
print(*my_list[2])


#3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   # - получите сумму всех чисел,
   # - распечатайте все строки, где есть буква 'a' !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100, True, 'lol']
print(sum([i for i in list_1 if str(i).isdigit()]))
for item in list_1:
    if type(item) == str:
        if 'a' in item:
            print(item)


#3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
my_list = ['cat', 'dog', 'horse', 'cow']
my_tuple = tuple(my_list)
print(my_tuple)

'''
3.4. Напишите программу, которая определяет, какая семья больше. 
      1) Программа имеет два input() - например, family_1, family_2. 
      2) Членов семьи нужно перечислить через запятую. 
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
'''
family_1 = input('Перечислите членов Вашей семьи через запятую: ').split(',')
family_2 = input('Перечислите членов Вашей семьи через запятую: ').split(',')


if len(family_1) == len(family_2):
    print('Equal')
elif len(family_1) > len(family_2):
    print(f'Первая семья больше, в ней {len(family_1)} человек')
elif len(family_2) > len(family_1):
    print(f' Вторая семья больше, в ней {len(family_2)} человек')


'''
3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме. 
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение
'''

my_dict= {
    'title': 'Twin Peaks',
    'director': 'David Lynch',
    'year': 1990,
    'budget': 100000,
    'main actor': 'Kyle MacLachlan',
    'slogan': 'A town where everyone knows everyone and nothing is what it seems'
}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())


# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(my_dictionary.values())
print(sum(my_dictionary.values()))


#3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
my_list = [1, 2, 3, 4, 5, 3, 2, 1]
my_set = set(my_list)
print(my_set)


'''
3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга 
'''
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

print(set2.intersection(set1))

print(set1.difference(set2), set2.difference(set1))


print(set1.issubset(set2))
print(set2.issuperset(set1))

#REVIEW

#SORT AND SORTED
list_1 = [1,3,6,4,7]
list_1.sort()
print(list_1)
#OR
print(sorted(list_1))

#LIST COMPREHENTION
new = [x*x for x in list_1 if x%2 == 0]
print(new)

new_2 = []
for x in list_1:
    if x % 2 == 0:
        new_2.append(x * x)
print(new_2)

#TUPLES
tuple_0 = ('Mark',)
tuple_1 = ('Mark', 26, ['314 N 11Ln', 'Los Angeles', 85954])
list_3 = list(tuple_1) #МОЖНО КОНВЕРТИРОВАТЬ В ЛИСТ, ИЗМЕНИТЬ ДАННЫЕ, КОНВЕРТИРОВАТЬ ОБРАТНО
print(list_3)
list_3[1] = 27
print(list_3)
tuple_1 = tuple(list_3)
print(tuple_1)
tuple_1[2][-1] = 85955
print(tuple_1)#МОЖНО ИЗМЕНИТЬ ЛИСТ, ЕСЛИ ОН ВКЛЮЧЕН В tuple

#------------

list_1 = [1,3,6,4,7,1,1]
print(set(list_1))#ПЕРЕВЕСТИ В set ЧТОБЫ УДАЛИТЬ ДУБЛИКАТЫ И ОТСОРТИРОВАТЬ

#------------

list_1 = [1,3,6,4,7] #СДЕЛАТЬ ИЗ ЛИСТА СЛОВАРЬ

dict_1 = {}
for i in range(len(list_1)):
    dict_1[i] = list_1[i]
print(dict_1)
print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())

for ind, val in enumerate(dict_1.items()):
    print(f'{ind} ----> {val}')

print(dict_1.get(1))


