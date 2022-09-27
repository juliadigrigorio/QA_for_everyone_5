# OOP
class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def work(self):
        return 'I can work'

class Developer(Employee):  #НАСЛЕДОВАНИЕ. ПОДКЛАСС КЛАССА Employee
    def __init__(self, name, surname, language):
        super().__init__(name, surname)
        self.language = language

    def work(self):
        return 'I am coding'


class Tester(Employee):
    def __init__(self, name, surname, language, test_framework ):
        super().__init__(name, surname)
        self.language = language
        self.test_framework = test_framework

    def work(self):
        return 'I can write tests'



dev1 = Developer('Max', 'Frolov', 'Python')
print(dev1.work())
print(dev1.name)
print(type(dev1))
print(issubclass(Developer, Employee))

tester1 = Tester('Anna', 'Fedorova', 'Java', 'TestNG')
print(tester1.work())
print(tester1.language)




employee1 = Employee('Alex', 'Smith')
print(employee1.name)
print(employee1.surname)
print(employee1.work)


employee2 = Employee(name='Vladimir', surname='Popov')
print(employee2.name)
print(employee2.surname)