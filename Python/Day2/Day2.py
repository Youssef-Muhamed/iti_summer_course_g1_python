# lists
# 1. ordered
# 2. mutable (changeable)

# myListNums = list([1, 2, 3, 4, 5])
# myList = ['ahmed','zaher','mohamed',(1,2,3)]
# myList2 = ['test']
# myList.sort()
# myList.reverse()
# myList.pop()
# removed_el = myList.pop(0)
# myList.append('mahmoud')
# myList.insert(1,'mahmoud')
# myList.extend(myList2)
# finalList = myList + myList2
# del myList[:]
# print(sum(myListNums))
# print(5 in myListNums)
# print(myList)

######################################
# tuples
# 1. ordered
# 2. immutable => cannot be changed
# myTuple = ('ahmed','zaher','mohamed')
# myTuple[0] = 'mahmoud'
# print('ahmed' in myTuple)

######################################
# sets
# 1. unordered
# 2. mutable => cannot be changed
# 3. unindexed
# mySet = {'ahmed','zaher','mohamed',(1,2,3)}
# mySet.add('mahmoud')
# mySet[0] = 'mahmoud'
# print(mySet)

######################################3
# dictionaries
# 1. unordered
# 2. mutable => can be changed
# 3. indexed
# myDict = {'name':'ahmed','age':25,'address':'cairo'}
# # myDict['name'] = 'mahmoud'
# myDict.update({'area':'october'})
# del myDict['age']
# print(myDict.keys())
# print(myDict.values())
# print(myDict.items())
# myDict.clear()
# print(myDict)

################################
# loops
# 1. for
# 2. while

# print(range(10))
# for i in range(0,10):
#     if i == 5:
#         continue
#     print(i)
# for index,item in myDict.items():
#     print(index,item)

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# for i in range(10):
#     print(i)
# else:
#     print('done')

#################################
# myString = 'ahmed zaher mohamed'
# if 'ahmed' in myString:
#     pass
# def myFunc():
#     pass
# class myClass:
#     pass

# myInput = input('Enter your name: ')
# print(type(int(myInput)),myInput)


# while True:
#     myInput = input('Enter your pwd: ')
#     if len(myInput) < 5:
#         print('Password should be at least 5 characters')
#         continue
#     else:
#         print('Password is valid')
#         break

# mynum = 'a10'

# print(type(int(mynum)))
# 64
# str                  int
# 00000101 0000100     0100000
# change in data representation

#####################################
# Functions
# def myFunc():
#     print('hello world')
#
# myFunc()

# def doSumm(num1,num2):
#     return num1 + num2
#
# sum = doSumm(10,20)
# print(sum)
# def doSumm(num1,num2=10):
#     print(num1+num2)
# doSumm(num2=10,num1=20)

# my_input = input('Enter your calc: ')
#
# def doSumm(*args):
#     print(eval(args[0]))
#
# # doSumm(my_input)
# print(10+20*100)
# print('test','test2')

# def doSumm(*args,**kwargs):
#     print(kwargs)
#     print(args)
# doSumm(20,num1=10,num2=20)
########################################
# Scoping

# myVar = "Ahmed"
# def myFunc():
#     myVar = "Zaher"
#
#     def myInnerFunc():
#         nonlocal myVar
#         myVar = "Ali"
#         print(myVar)
#     myInnerFunc()
#     print(myVar)
#
#
# myFunc()
# print(myVar)
#
################33
# print('Hello from iti')
# print(10 / 0)
# print('Hello from iti')

# num = 10
# try:
#     print(num / 0)
# except Exception as e:
#     raise Exception(f'error => {e}')
# else:
#     print('no error')
# finally:
#     print('finally')
##################################################3
# from say_hello import *
# from datetime import datetime
# import say_hello
# say_hello_func()
# print(do_sum(10,20))
# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %p'))
def myFunc2(name):
    print(name)

def myFunc(name):
    mayVar = "Ahmed"
    myFunc2(name)
    print('hello world')
    mayVar = name + mayVar
    print(mayVar)

myFunc('mohamed')










