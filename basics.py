# # Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
# # Type "help", "copyright", "credits" or "license()" for more information.
# age = 110
# print(age)
# 110
# a,b,c = 10,20
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     a,b,c = 10,20
# ValueError: not enough values to unpack (expected 3, got 2)
# a,b,c = 10, 20, 30
# print(a,b,c)
# 10 20 30
# e,f,g = 10, 20, "work"
# print(e,f,g)
# 10 20 work
# c = a + b
# print(c)
# 30
# typeof(a)
# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     typeof(a)
# NameError: name 'typeof' is not defined. Did you mean: 'type'?
# type(a)
# <class 'int'>
# type(g)
# <class 'str'>
# a = b = c = 10
# print(a,b,c)
# 10 10 10
# FILE_SIZE_LIMIT = 1000
# print(FILE_SIZE_LIMIT)
# 1000
# emp_id = 11
# name = 'Nonso'
# salary = 2000.00
# print("My employee id is", emp_id)
# My employee id is 11
# print("My name is ", name)
# My name is  Nonso
# print()

# print("My salary is ", salary)
# My salary is  2000.0
# print(2e2)
# 200.0
# print(205e2)
# 20500.0
# print(20e2)
# 2000.0
# print(2.05e4)
# 20500.0
# print(1.576e6)
# 1576000.0
# print(1.576e5)
# 157600.0
# a = 3 + 5j
# b =  2 - 5.5j
# c = 3+10.5j
# print(a)
# (3+5j)
# print(b)
# (2-5.5j)
# print(c)
# (3+10.5j)
# print(a + b)
# (5-0.5j)
# print(b + c)
# (5+5j)
# print(c + a)
# (6+15.5j)
# a = True
# b = False
# print(a)
# True
# print(b)
# False
# print(a + b)
# 1
# print(a + a)
# 2
# a = None
# print(a)
# None
# print(type(a))
# <class 'NoneType'>
# x = [10, 20, 100, 40, 15]
# y = bytes(x)
# print(type(y))
# <class 'bytes'>
# print(y[0])
# 10
# print(y[1])
# 20
# print(y[2])
# 100
# print(y[3])
# 40
# print(y[4])
# 15
# print(y[5])
# Traceback (most recent call last):
#   File "<pyshell#55>", line 1, in <module>
#     print(y[5])
# IndexError: index out of range
# y[1] = 25
# Traceback (most recent call last):
#   File "<pyshell#56>", line 1, in <module>
#     y[1] = 25
# TypeError: 'bytes' object does not support item assignment
# for a in y:
#     print(a)

    
# 10
# 20
# 100
# 40
# 15
# a = range(5)
# print(a)
# range(0, 5)
# for x in a:
#     print(x)

    
# 0
# 1
# 2
# 3
# 4
# b = range(1, 10)
# for x in b:
#     print(x)

    
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# c = range(1, 15, 2)
# for x in c:
#     print(x)

    
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 2**
# SyntaxError: incomplete input
# a = 2**
# SyntaxError: incomplete input
# a = 2 ** 3
# print(a)
# 8
# a = 2 ** 4
# print(a)
# 16
# print(0 and 4)
# 0
# print(5 and 7)
# 7
# print(21 and 0)
# 0
# >>> print(15 and 8)
# 8
# >>> 15 and 8 and 5
# 5
# >>> not 5
# False
# >>> text = "Welcome to python programming"
# >>> print("Welcome", in text)
# SyntaxError: invalid syntax
# >>> print("Welcome" in text)
# True
# >>> print("welcome" in text)
# False
# >>> print("nonso" in text)
# False
# >>> print("Han" not in text)
# True
# >>> a = 25
# >>> b = 25
# >>> print(id(a))
# 140703442462248
# >>> print(id(b))
# 140703442462248
# >>> b = 28
# >>> print(id(b))
# 140703442462344
# >>> a is b
# False
# >>> a is not b
# True
# >>> name = input("Enter your first name: ")
# Enter your first name: nonso
# >>> print("Your entered the name as: ", name)
# Your entered the name as:  nonso
# >>> 
# ========================================== RESTART: C:/Users/chukwunonso.molokwu/Desktop/Python practice/age.py =========================================
# Enter your age: 66
# Your age is : 66
# age type is  <class 'str'>
# Converting and printing type:  <class 'int'>
# a = "Python"
# b = 3
# print(a*b)
