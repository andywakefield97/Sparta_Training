# Collections are Lists, Tuples, Dictionary, Sets and Frozen Sets.
#Lists are ordered and changeable - Allows duplicate members

# #Task 1
# Number_list = [10,111,24,56,78,75,65,80]
# odd_list = []
# even_list = []
#
# for m in Number_list:
#     if int((m % 2)) > 0:
#         even_list.append(m)
#     elif int((m%2))==0:
#         odd_list.append(m)
#
# print(odd_list)
# print(even_list)

# Tuple is a collection which is ordered and unchangeable and allows duplicate members
#
# essentials = ('bread', 'cheese', 'eggs')
# print(essentials)
# print(essentials.count('cheese'))

#Dictionary is a collection which is unordered, changeable and indexed

# student_1 = {
#     "name": "andy",
#     "stream": "data",
#     "lessons_completed": 4,
#     "names_completed_lessons": ["variables", "data_types", "sql", "agile"]
# }
#
# print(student_1)
# print(student_1["stream"])
# print(student_1["names_completed_lessons"][1])
#
# #Changing values
#
# student_1["lessons_completed"] = 3
# print(student_1["lessons_completed"])
#
# #Removing
#
# student_1["lessons_completed"].remove("stream")

#Set is a collection which is unordered and unindexed

# car_parts = {"wheels", "steering wheel", "doors", "exhaust"}
# #
# # car_parts.add("windshield")
# #
# # car_parts.remove("doors")
# #
# # print(car_parts)

#Control flow

#For IF statements, For statements and While loop
# age = 34
# if (age <19):
#     print("you are not eligble to watch this film")
# elif (age>19):
#     print("you are okay to watch the film")
#
#
# age = int(input("What is your age?"))


#*TASK*
# film_rating = input("what is the rating?")
#
# if film_rating == "universal":
#     print("all age groups can watch this film")
# elif film_rating == "pg":
#      print("General viewing, but some scenes may be unsuitable for young children.")
# elif film_rating == "12" or film_rating == "12a":
#     print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
#
# elif film_rating.lower() == "15":
#         print("No one younger than 15 may see a 15 film in a cinema.")
# elif film_rating.lower() == "18":
#      print("No one younger than 18 may see an 18 film in a cinema.")
# else:
#      print("this is not a correct rating, please use universal, pg, 12, 12a, 15, 18")

#*FIZZBUZZ TASK*#
# number = int(input("What number do you want to FizzBuzz?"))
#
# if (number%5) == 0 and (number%3) == 0:
#     print("Fizzbuzz")
# elif (number%3) == 0:
#     print("Fizz")
# elif (number%5) == 0:
#     print("Buzz")
# else:
#     print("Failure")

#*FOR LOOPS*#

# fruits = ["apple", "pear", "banana"]
#
# for x in fruits:
#     print(x)
#
# for x in "banana":
#     print (x)
#
# for x in fruits:
#     print(x)
#     if x == "pear":
#         break
#
# for x in range (101):
#     print(x)


# city = ["dortmund", "madrid", "manchester"]
# football = ["tiki taka", "long ball", "park the bus"]
#
# for x in city:
#     for y in football:
#         print(x,y


list = [2,3,4,5,6,7]
embedded_list = [[1,2,3],[4,5,6]]
dict = {1: {"name":"Andrew", "money":"£4545353333"}, 2: {"name":"Gemima", "money":"£45000"}}
# for x in embedded_list:
#     print(x)
#     for y in x:
#         print(y)


# for value in dict:
#     print(value)
#
# for value in dict.values():
#     print(value)
#
# for value in dict.values():
#     for x in value.values():
#         print(x)


#WHILE LOOPS
#
# x=5
#
# while x<10:
#     print(f"its working --> {x} ")
#     x=x+1

##