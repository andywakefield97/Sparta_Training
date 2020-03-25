#Functions are a special relationship where each input has single output

# def hello():
#     print('hello')
# hello()
#
# def func(a,b):
#     return a+b
# print('The sum is', func(23,45))
#
# def funct(a=10,b=20):
#     return a*b
# print(funct())

# def add(a,b):
#     return a+b
#
# def multiplication (x,y):
#     return x*y
#
# def subtraction (x,y):
#     return x-y
#
# def division (x,y):
#     return x/y
#
# print(multiplication(2,5))
# print(subtraction(10,5))
# print(division(45,9))

#Classes are a way of bringing both data and functionality together
#When a function is declared in a class it is called a method
# class Dog:
#
#     animal_kind = 'canine' #Class Variable
#
#     def bark():
#         return 'woof'
#
#     def __init__(self,name):
#         self.name = name
#
# print(Dog.animal_kind)
# print(Dog.bark())
#
#
# class Car:
#
#     model = 'Tesla'
#
#     def engine(self):
#         return ('Vroom Vroom')
# #
# car1 = Car()
# print(car1.engine)

# class Fizzbuzz:
#
#     def calculation(number):
#         if (number%5) == 0 and (number%3) == 0:
#             print("Fizzbuzz")
#         elif (number%3) == 0:
#             print("Fizz")
#         elif (number%5) == 0:
#             print("Buzz")
#         else:
#             print("Failure")
#
# Fizzbuzz.calculation(15)

# class Student:
#     student_type = 'Trainee'
#
#     def enrol(self):
#         print('Yesss')
#
# print(Student.student_type)
# print()


# class Animal():
#
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
#
#     def animal_sound(self):
#         if self.type == 'Giraffe':
#             return ('Neighhhhhhh')
#
#     def jump(self):
#         if self.type == 'Horse':
#             return ('Yes, a {} can jump').format(self.type)
#         elif self.type == 'Giraffe':
#             return ("No, a {} can't jump").format(self.type)
#
#
# x = Animal('Dave', 'Giraffe')
# y = Animal('Jon', 'Horse')
#
#
# print(x.name, 'The', x.type)
# print(x.animal_sound())
# print(x.jump())
# print(y.name, 'The', y.type)
# print(y.jump())


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



# import random
# import math
#
# num = 23.87
#
# print(random.random())
# print(math.floor(num))
# print(math.ceil(num))
#
# import requests
# request_bbc = requests.get("https://www.bbc.co.uk/")
# print(request_bbc.content)



#Four pillars of Object oriented programming
# Abstraction, Inheritance, Encapsulation and Polymorphism
# Abstraction is displaying only essential information to the user and hiding the details from the user
#Inheritance is the mechanism in which one class acquires the property of another class.