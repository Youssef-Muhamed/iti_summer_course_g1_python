# Files
# myFile = open("file.txt", "r")
# myFile.seek(1)
# myListFile = myFile.read().split(' ')
# print(myListFile)
# print(myFile)
# myFile = open("file.txt", "a")
# print(myFile.read())
# myFile.write("\nHello World")

# myFile.seek(10)
#
# myFile.write("Hello ITI")
# myFile.close()
# def login(uname, upwd):
#     myFile = open("file.txt", "r")
#     users = myFile.read().split('\n')
#     for user in users:
#         if user == "":
#             continue
#         name, pwd = user.split(":")
#         name = name.strip()
#         pwd = pwd.strip()
#         if uname == name and upwd == pwd:
#             return True
# while True:
#     option = input("Enter 1 to add user or 3 to login or 2 to exit: ")
#     if option == '2':
#         break
#     if option == '1':
#         name = input("Enter your name: ")
#         pwd = input("Enter your pwd: ")
#         myFile.write(f"\n{name}:{pwd}")
#         print("User added successfully")
#     if option == '3':
#         name = input("Enter your name: ")
#         pwd = input("Enter your pwd: ")
#         if login(name, pwd):
#             print("Login successful")
#         else:
#             print("Login failed")
#             continue
############################
# import os
# print(os.system("pwd"))
# import math
# print(math.pi)
# print(math.ceil(2.5))
# print(math.floor(2.5))
# print(math.sqrt(9))

# import re
# pattern = '[a-z]+'
# if re.search(pattern, "123"):
#     print("found")
# else:
#     print("not found")
# import random
# print(random.randint(1, 10000))
# print(random.random())
# from datetime import datetime
# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %p'))
# print(datetime.today())
###########################################
# decorator
# def myDecorator(myFunc):
#     def wrapper():
#         print("before")
#         myFunc()
#         print("after")
#     return wrapper
#
# def myDecorator2(myFunc):
#     def wrapper():
#         print("myDecorator2 before")
#         myFunc()
#         print("myDecorator2 after")
#     return wrapper


# @myDecorator2
# @myDecorator
# def myFunc():
#     print("Hello from iti")
# myFunc()

# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return
#
#         return func(a, b)
#     return inner
#
# @smart_divide
# def divide(a, b):
#     print(a/b)
#
# divide(2,5)
#
# divide(2,0)
