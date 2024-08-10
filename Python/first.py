

# low     -> assembly 8086,8085, 100 embeded prog / human cant understand
# middle  -> c lang, micro / human 
# high    -> python , general purpose human understand

# 1989 dev. neth national reasearch inst - guido van rossam
# 20 feb 1991 avail for public.

# easy to learn 
# --------------
# print("Hello")
# python3 core-python.py -> mac
# py core-python.py      -> win

# print("1 Hello")
# print("2 Hello")
# print("3 Hello")
# print("4 Hello")
# print("5 Hello")

# print("10+20")
# 30
# 1020

# print(10+20)
# print(10+20/5*4-1)
# 10+20/5*4-1
# 10+4*4-1
# 10+16-1
# 26-1
# 25

# 2 , 23, 10
# 80% math -> logic 

# print("i am printing somthing")
# print('i am 

# printing 
# somthing')

# string literal
# print('''i am 

# printing 

# somthing''')
# print("""i am 
# printing 
# somthing""")

# where we can use python
# accept mobile application 


# Features of python 
# 1) simple & easy to learn 
# 2) open source 
    # android -> vivo , sumsung, oppo, oneplus
# 3) platform independent
    # 
# 4) portability 
# 5) Dynamic type
    # int i;  c, c++, java
# 6) extensive lib support
#   more than 140000 

# python version 1.0    1994
# python version 2.0    2000
# python version 3.0    2008 wont provide back compatibility

# print(10+20/5*4-1)

# a=10
# b=20
# c=5
# d=4
# e=1
# z = a+b/c*d-e
# print("a+b/c*d-e :",z)

# a=10
# b=20
# z1=a+b
# z2=a*b
# z3=a/b
# z4=a-b
# print("a+b =",z1)
# print("a*b =",z2)
# print("a/b =",z3)
# print("a-b =",z4)

# Q-1 find area of circle 
# 3 pizza 
# 2 6"      
# 1 9"

# r = 3
# pi = 3.14
# area_of_circle = pi*r*r
# print("area of circle : ",area_of_circle)

# 1. Python program to find Simple Interest
# SI  = (p*r*n)/100
# 2. Python program to Calculate Area of Square 
# l*l
# 3. Python program to Calculate Area of Rectangle
# l*b
# 4. Python program to Calculate Area of Triangle
# 0.5*b*h


# identifiers 
# print()  # function -> () -> indentifier

# Variable
# Variable is storage location / container that contain some value that can be varied.

# 1) a - z , A -Z  , 0 - 9
# 2) start with _ ->  private variable
# 3) cant start with 0 - 9.
# 4) case sensitive aoc /AOC /Aoc / AoC
# 5) keywords / reserved words cant use as variable
#   #) logical naming conversion

# import keyword
# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# how take input from user ?

# str = int(input("Enter your string "))
# print(type(str))
# python takes string as default input
# a = int(input("Enter a : ")) # str - int
# b = int(input("Enter b : "))
# print(" a+b :",a+b)

# -------------------
#     Data Types
# -------------------

# data type represent type of data in variable 

# 122 4 54 6 3              number          int  
# 3.14 4.2 2.1              floating        float 
# d S T f D Y               char            -               
# pen Bike apple            string          str
# exam, ass, result         DS              ds - list , tuple, set, dict
# true false                boolean         bool


#1 int  
#2 float             
#3 str
#4 list
#5 tuple
#6 set
#7 dict
#8 frozenset
#9 bool
#10 bytes
#11 range 
#12 bytearray
#13 complex
#14 None

# Number System
# Binary        0 - 1
# octal         0 - 7
# Decimal       0 - 9
# Hexadecimal   0 - 9 , 10-A, 11-B, 12-C, 13-D, 14-E, 15-F

#1 int  
# var1 = 0b101
# var1 = 0o101
# var1 = 0Xff
# print(var1)
# bin()
# oct()
# hex()

# var3 = 0b101.01
# print(var3)

#2 float      
# var1 = 22
# var2 = 7
# print(var1/var2) 
# float represents only in decimal form

#3 str
#4 list
#5 tuple
#6 set
#7 dict
#8 frozenset

#9 bool
# print(10>20)
# print(type(10>20))

#10 bytes
#11 range 
#12 bytearray
#13 complex
# var1= 10+1.5j
# var2= 20+1.5j
# print(var1+var2)
# print(type(var1+var2))
#14 None

# Type conversion
# a=3.14
# print(type(a))
# print(a)
# b=int(a)
# print(type(b))
# print(b)

# print(type(True))
# print(int(True))
# print(int(False))

# a="A"
# a="10"
# a="10.10"
# print(a)
# print(type(a))
# b = int(a)
# print(b)
# print(type(b))

# -------------------
#    Operators
# -------------------
# +, -, = ,   
# Operator is a symbol that performes certain operations.

# 1. Arithmatic
# 2. Relationlal
# 3. Logical
# 4. Bitwise 
# 5. Assignement 
# 6. special operator

# 1. Arithmatic
# +,-,*,/,% - modulus ,
# // -> floor divison
# ** -> exponent / power
# print(10%3)
# print(80%9)

# print(22/7)
# print(22//7)
# print(27/7)
# print(27//7)

# # print(2**3)
# print(2**10)

# print(27//7)
# print(type(27//7))
# print(27.0001/7)
# print(27.0001//7)
# print(type(27.10//7))

# print("apple"**3)
# print("apple"*3)
# print(3.14**2)

# a+b , a*b+c -> arithmatic expression

# 2. Relationlal
# >     
# <= 
# < 
# >=

# == 
# !=
# print(10==10)
# print(10!=10)
# # !=
# print(101==10)
# print(101!=10)

# print(10<20)
# print(10<20<30>40)
# print(10>20>30)
# print(30>20>10)
# print(30<20<10)
# print(30<20<10)

# print(10<20>40)
# 10<20 and 20>40
# 1>40

# 3. Logical

# AND OR NOT
# gates

# x     y       x and y     x or y
# -----------------------------------
# 1     1           1           1
# 1     0           0           1
# 0     1           0           1
# 0     0           0           0

#  x    not x
#  0    1  
#  1    0    
# a=3.14
# print(type(a))
# print(type(not a))
# print(not a)

# print(not "")
# print(not "apple")

# print("" and "apple")
# print("twoapple" and "apple")
# print("apple" and "apple")

# print("" or "apple")
# print("apple" or "twoapple")

# 4. Bitwise 
# 5. Assignement 
# 6. special operator