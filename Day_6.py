# class Students:
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def year(self):
#         if self.age == '14':
#             return '{} is in Year 7'.format(self.name)
#         elif self.age == '12':
#             return '{} is in Year 5'.format(self.name)
#
#     def what_gender(self):
#         if self.gender == 'Male':
#             return '{} is male'.format(self.name)
#
#
# x = Students('Jack', '12', 'Male')
# y = Students('Jill', '14', 'Female')
#
# print(x.what_gender())
# print(y.year())



# class Smurf:
#     def __init__(self, height, age, weight):
#         self.height = height
#         self.age = age
#         self.weight = weight
#
#     def fat_or_skinny(self):
#         if self.weight <= 40:
#             return 'Skinny Smurf'
#         elif self.weight >40:
#             return 'Fat Smurf'
#
# smurf_1 = Smurf(45,2,65)
# smurf_2 = Smurf(56,4,39)
# smurf_3 = Smurf(52,5,86)
#
#
# print(smurf_1.fat_or_skinny())


#Four pillars of Object oriented programming
# Abstraction, Inheritance, Encapsulation and Polymorphism

# Abstraction is displaying only essential information to the user and hiding the details from the user
from Day_3 import *
#Inheritance is the mechanism in which one class acquires the property of another class.

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def talk(self):
        Nickname = input ('What is your nickname?')
        return ('Hi my name is {}'.format(Nickname))

person_1 = Person('Andrew', 'Wakefield')

print(person_1.talk())

#Encapsulation is an object oreitned python program you can restrict access to methods and variables. Preventing data from being modified by accident

# '__' before a method encapsulates so that it cannot be used by the subclass

#Polymorphism = Defines methods in the child class that have the same name as the methods in the parent class#
#It is possible to modify a method in a cgild class that is inherited from the parent class and this is called method overriding
# method overrriding is a type of polymorphism

#Lambda functions
#Lambdas are essentially anonymous function that can take multiple parameters but return only one expression

# def add (num1,num2):
#     return num1 + num2
#
# addition = lambda num1, num2:num1 +num2
#
# savings= [237,567,674,78]
#
# bonus= list(map(lambda x: x * 1.1, savings))
#
# print(bonus)

import pytest




