x = 5
if x == 5:
    print('Five')
elif x > 5:
    print('More than five')
else:
    print('Less than five')

#------------

i = 0
while i < 5:
    print('Hello, world!')
    #i = i + 1
    i += 1

#------------


i = 0
while i < 5:
    print('Hello, world!')
    if i == 3:
        break
    i += 1

#------------

name = input()
for letter in name:
    print(letter)

name = input()
for i in name:
    print(i)

#------------

name = 'Oleg'
print(name[2])
print(name[-1])

for i in range(5):
    print(1)

for i in range(5):
    print(i, 'Hi')
            # начало, конец, шаг
for i in range(1, 10, 2):
    print(i)

for i in range(2, 11,2):
    print(i)

for i in range(5, 1, -1):
    print(i)

#------------

name = 0
if name:
    print('True')
else:
    print('False')

#------------

name = 'Oleg'
if name:
    print('True')
else:
    print('False')

#------------

age = int(input('Enter your age: '))
if age >= 21 and age <= 40:
    print('Welcome')
elif age <= 13:
    print('Where is your mom?')
elif age >= 40:
    print('too old')
else:
    print("Go home, baby")

#------------

def give_me_power(num, n):
    return (num ** n)

print(give_me_power(2,5))
give_me_power(2,4)

#------------

#1
health = int(input())
if health <= 0:
    print(False)
else:
    print(True)



#2
num = int(input('Введите число: '))
if num % 2 == 0:
    print(f' {num} --  Четное')
else:
    print(f' {num} -- Нечетное')


#3
year = int(input('Enter year: '))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f'{year} високосный')
else:
    print(f'{year} не високосный')



#4
word = input('Enter your word: ')
times = int(input('How many times do you want to repeat: '))
for i in range(times):
    print(word)


#------------

#
string = input('Enter the word: ')
for i in string:
    print(i, end=' ')


for index in range(0, -10, -1):
    print(index, end=' ')

string = input('Enter your word: ')
for index in range(len(string)):
    print(index, end=' ')