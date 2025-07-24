# oop  --> object oriented programming
# blueprint or style of programming

# class --> blueprint
# method --> function
# property --> attribute

# class Student:
#     eye = 2
#     def __init__(self):
#         self.name = "Ahmed"
#         self.age = "55"
#
#     def say_hello(self):
#         print(f"Hello {self.name}")
#
#     @classmethod
#     def say_hello_2(cls):
#         print(f"Hello {cls.eye}")
#
#     @staticmethod
#     def say_hello_3():
#         print("Hello Static")
#
# obj1 = Student()
# print(obj1.name)
# obj1.name = "Zaher"
# print(type(obj1))
# obj1.say_hello()
# obj1.say_hello()
# Student.say_hello_3()

# myString = "Hello World"
# print(type(myString))
# obj2 = Student()
# print(obj2)

##########################################3
# Inheritance
#
# class Person:
#     def __init__(self):
#         print("======== Person Class ========")
#     def say_hello(self):
#         print("Hello from Person Class")
#
# class Teacher:
#     def __init__(self):
#         self.name = "Teacher"
#         print("======== Teacher Class ========")
#
# class Student(Teacher,Person):
#     def __init__(self):
#         super().__init__()
#         Person.__init__(self)
#         print("======== Student Class ========")



obj = Student()
print(obj.name)
# obj.say_hello()
# print(obj)





