
user_name = input('Enter your name: ')
age = int(input('Enter your birth year: '))
current_age = 2022 - age
print(f'Hello, {user_name}. Your age is: {current_age}')

#---------

snow = '*'
blank = ' '
print(snow * 10)
print(snow + (blank * 8) + snow)
print(snow + (blank * 8) + snow)
print(snow * 10)

#----------

print(' ' + snow * 10, '\n', snow + (blank * 8) + snow, '\n', snow + (blank * 8) + snow, '\n', snow * 10)



#---------

m = input('Digit and string: ')
print(m)
m = m.isdigit()
m = m.upper()
m = m.isalpha()
print(m)

#---------
a = input('Enter your name: ')
print(f'Hello, my dear {a}!')
print('Hello, my dear' + ' ' + a.format() + '!')
print('Hello, my dear' + ' ' + a + '!')