# create a variable
#x = 1
#print(x)
'''
a=1
b=2
c=3.5
hi="hello world"

print(hi)'''

'''print("what is your name")
name = input()
print('Hi')
print(name)'''

#*AGE/DOB/ADDRESS EXERCISE*

# print('Hello, What is your full name?')
# full_name = input()
# print('hello ', full_name)
# print('What is your date of birth?')
# dob = input()
# print('What is your full address?')
# address = input()
# print("These are your details")
# print(full_name, dob, address)

# FloatNum = 1.346
# IntNum = 4
# name = "xyz"
# print(FloatNum*IntNum)
# print(str(IntNum)+name)

# Wow = 'I said "Wow"'
# print(len(Wow))

# a= True
# b = False
#
# print(a!=b)
# print(a>=b)
# print(b<=a)

# hi = "Hello World"
#
# print(hi.isalpha())
# print(hi.islower())
# print(hi.endswith("!"))
# print(hi.startswith("H"))

# print(bool(1))
# print(bool(None))


# a = 45
# b = 50
#
# if (a<b) :
#     print("{} is bigger".format(a))
# else:
#     print("{} is bigger".format(b))


#*BIGGEST NUMBER EXERCISE*

# a = input("Type a number")
# b = input("Type another number")
# c = input("Type a final number")
#
#
#
# if (a>b) and (a>c) :
#     print("{} is bigger than {} and {}".format(a,b,c))
# elif (b>a) and (b>c):
#     print("{} is bigger than {} and {}".format(b, a, c))
# elif (c>a) and (c>b):
#     print("{} is bigger than {} and {}".format(c,a,b))
# elif (a = b = c) :
#     print("A, B and C are equal")

#
# list_data = [1,2,3,4,5]
#
# for m in list_data:
#     print(m*2)




test_list = [4,8,12,16,20,24,28,32,36,40]
new_list = []
for m in test_list:
    if m >15 :
        new_list.append(m)
    else:
        continue


print(new_list)


