# class Person:
#     def __init__(self):
#         self.__name = "Ahmed"
#
#         # setter
#     def set_name(self, name):
#         self.__name = name
#
#     # getter
#     def get_name(self):
#         return self.__name
#     @property
#     def p_name(self):
#         return 'Zaher'
#
# class Student(Person):
#     def print_name(self):
#         print(self.name)
#
# obj = Person()
# print(obj.p_name)
# print(obj.get_name())
# obj.set_name("Zaher")
# print(obj.get_name())

# obj.print_name()


# Access Modifiers
# Public
# Protected
# Private

######################################################
# Abstraction
from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class Student:
    age = 10
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name

    def __call__(self):
        print(f"Hello {self.name}")

    def __len__(self):
        return len(self.name)

    @classmethod
    def get_age(cls):
        return cls.age

obj = Student("Omar")
# obj()
# print(obj.get_age())
# print(len(obj))
myString = "Omar"
print(type(myString))
print(len(myString))