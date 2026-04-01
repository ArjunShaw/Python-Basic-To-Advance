# Hello This is a single line comment.
"""Hello, There are not multiple line comment in pythopn but we can use using Doc string"""

# print("Namastey Youtube we're learning python")

# name = "Arjun"
# age = 22

# print(name, age)
# print(type(name), type(age)) # type checking



"""Data Types in python"""
#Numbers ===============================>

# a = 12
# b = 3.23
# c = 12/3
# d = 32j

# print(type(a)) # <class 'int'>
# print(type(b)) # <class 'float'>
# print(type(c)) # <class 'float'>
# print(type(d)) # <class 'complex'>

# string =======================================>
# str = "1234Arjun@@"
# print(type(str))   # <class 'str'>

# # Boolean =============================>
# b = True
# v = False
# print(type(b))  # <class 'bool'>  
# print(type(v))  # <class 'bool'>


"""String"""
#Unicode =====================================================>
# a = "A"
# print(ord(a)) # To check the unicode of A is ==> 65

# b = 65
# print(chr(b)) # TO change the unicode into character ==> A 

# Indexing print charcter ==========================================>
# a = "arjun"
# print(a[1]) # using positive indexing == r
# print(a[-2]) # using Negative  indexing == u

# Slicing the string =====>
# a = "sher coder"
# print(a[0:4:1])
# print(a[5:10:1])
# print(a[5::])
# print(a[1:3:1])
# print(a[6:9:1])


"""Type Conversion """
# a = 13
# a = str(a)
# a = float(a)
# a = bool(a)

# b = "36"
# b = int(b)

# print(type(a))

"""Formaed output or not (input or ouput)"""
# name = "Arjun"
# age = 22

# print("Hello, My name is ",name, "and my age is ", age) #Not Formated
# print(f"Hello, My name is {name} and my age is {age}") # Formated Print Statement using f

#input =================================================>
# a = int(input("Hello, What's your age is : "))
# print(f"Hii, My age is {a}")

# num = int(input("Enter any number : "))
# print(F"you have enterd number {num} ")

"""Operators"""
# Arithematic op======================================>
# a = 20
# b = 5

# print(a+b) # 25
# print(a-b) # 15
# print(a*b) # 100
# print(a/b) # 4.0
# print(a%b) # 0
# print(a//b) # 4
# print(a**b) # 400  a = 20. b = 2

# Assignment op================================================>

# a = 20
# a += 40
# a += 60

# print(a)


# Comparision  op==== >  always provide boolean (true or false)
# a = 10
# b = 20
# print(a != b)


# Logical  op==== >

# print(123 > 23 and 34 < 34)
# print(123 > 23 or 34 < 34)
# print(not 34 == 34)

"""Question 1"""
# print(True and bool(0)) # True 




"""Conditionals Statements (if - else)"""
# num = int(input("Choose the number : "))
# if num > 10:
#     print("DO Task A")
# else:
#     print("Do Task B")

"""Questions"""
#1. =================================================>
# num1 = int(input("Enter your First number : "))
# num2 = int(input("ENter your Second number : "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num2:
#     print(f"{num2} is greater than {num1}")
# else:
    # print("Both numbers are same")
    
# 2.= ==================================================>
# gender = input("Enter the gender : ")
# if gender == "M" or gender == 'm':
#     print("Good morning Sir")
# elif gender == "F" or gender == 'f':
#     print("Good Morning Mam")
# else : 
#     print("Invalid Gender")

# 3. ===================================================>
# num = int(input("Enter any integer number : "))

# if num % 2 == 0:
#     print(f"The {num} number is Even")
# else:
#     print(f"The {num} number is odd")

#4. ======================================================>
# name = input("Enter your name : ")
# age = int(input("Enter your age : "))

# if age >= 18:
#     print(f"Hello {name}, You are a valid voter")
# else : 
#     print(f"Hello {name}, Your are not a valid voter")

# 5. ========================================================> 
# year = int(input("Enter a year : "))
# if year % 400 == 0  or year % 4 == 0 and year % 100 != 0: 
#     print(f"{year} is a leap year")
# # elif  :
# #     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# 6. =================================================================>
# temp = int(input("Enter a temprature : "))
# if temp < 0:
#     print("Freezing Cold")
# elif temp >= 0 and temp < 10:
#     print("Very Cold")
# elif temp >= 10 and temp <20 :
#     print("cold")
# elif temp >= 20 and temp <30 :
#     print("plesant")
# elif temp >= 30 and temp <40 :
#     print("hot")
# else:
#     print("Temperature is very hopt")
    
# ===============================================================================>
"""LOOPS"""

# range("Start", "Stop", "Steps") that 3 things are given in range(do iterate one by one)

# Syntax of for loop =========>
# for i in range(1, 21, 1): 
#     print(i)

# a = range(1, 21, 1)  same method like previous

# for i in a:
#     print(i)

# example ========================================================================>
# for i in range(21): # we need to give only stop value beacuse start and stop values are (default(values ==> 0, stop, 1)). that's why 
#     print(i)

# Reverse Order
# for i in  range(20, 0, -1):
#     print(i)

# for i in range(-5, -16, -1):
#     print(i)

# let's print a table of 5
# for i in range(5, 51, 5):
#     print(i)


# let's print a table of 5 using user input
# n = int(input("Which table do you want ? : "))
# for i in range(n, n*10+1, n):
#     print(i)

# for loop for String =============> Method One(1) ========>
# a = "prem chopra is my friend"
# # print(len(a)) # for calculating the length of string. len start adding from 1 index while(jabki) normal index start from 0
# for i in range(len(a)):
#     print(a[i]);


# for loop for String =============> Method Two(2) ========>
# a = "prem chopra is my friend"

# for i in  a:
#     print(i)


"""Break And Continue"""
# print("Break the number")
# for i in range(1, 21):
#     if i == 15:
#         break
#     else:
#         print(i)

# print("Countinue the number")
# for i in range(1, 21):
#     if i == 15:
#         continue
#     else:
#         print(i)


"""Question For loops"""
# # 1. =====================================>
# n = int(input("Enter an integer number : "))
# for i in range(n):
#     print("Hello WOrld")


## 2. ======================================> 
# num = int(input("Enter a number : "))
# for i in range(1, num+1):
#     print(i)

## 3. ======================================> 
# num = int(input("Enter number to print reverse : "))
# for i in range(num, 0, -1):
#     print(i)

## 4. ======================================> 
# num = int(input("Enter a number to print table : "))
# for i in range(num, num*10+1, num):
#     print(i)


# for i in range(1, 11):
#     print(f"{num} * {i} = {num*i}")

# 5. ======================================> 
# n = int(input("Enter a number to calculate sum of n terms : "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
#print(f"your sum is {sum})

# ## 6. ======================================> 
# num = int(input("Enter a number to calculate facotrial num : "))
# fact = 1;
# for i in range(1, num+1):
#     fact *= i
# print(fact)


# ## 7. ======================================> 
# num = int(input("Enter a number  : "))
# even = 0
# odd = 0
# for i in range(1, num+1):
#     if i % 2 == 0:
#         even += i
        
#     else:
#         odd += i
# print(f"Print sum of all even number {even} and odd numbers {odd}")

# ## 8. ======================================> 
# num = int(input("Enter a number  : "))

# for i in range(1, num+1):
#     if num % i == 0:
#         print(i)


# ## 9. ======================================> 
# num = int(input("Enter a number  : "))
# sum = 0
# for i in range(1, num):
#     if num % i == 0:
#        sum += i;

# # print(f"Sum factors are {sum}") 
# if sum == num :
#     print(f"Your number is perfect number : {num} ")
# else:
#     print("Your number is not perfect")


# ## 10. ======================================> 
# num = int(input("Enter a number  : "))
# count = 0
# for i in range(1, num+1):
#     if num % i == 0:
#         count += 1
# # print(count)
# if count == 2:
#     print("This is a prime number")
# else:
#     print("This is not  a prime number")


# ## 11. ======================================> 
# str = input("Enter any stirng : ") # to reverse a string
# b = ""
# for i in range(len(str)-1, -1, -1):
#     # print(str[i])
#     b += str[i]   # to store and pritn string in one line
# print(b)


# ## 12.  ======================================> 
# str = input("Enter a string to check palindrome : ")
# b = ""
# for i in range(len(str)-1, -1, -1):
#     b += str[i]
    
# if b == str:
#     print("Your string is palindrome")
# else:
#     print("Your stirng is not palindrome")

# ## 13.  ======================================> 
# str = input("Enter any kind of word what you want : ")

# digit = 0
# alpha = 0
# spchar = 0

# for i in str :
#     if i.isdigit():
#         digit += 1
#     elif i.isalpha():
#         alpha += 1
#     else:
#         spchar += 1
# print(f"Your digits are {digit}\nYour alphabets are {alpha}\nYour special Character are {spchar}")



"""While Loop"""
# 1. ======================================>
# a = 1
# while a <= 30:
#     print(a)
#     a += 1

#2. ==================================================>
# a = int(input("Enter any number : "))

# while a > 0:
#     print(a % 10)
#     a //= 10


#3. ==================================================>
# a = int(input("Enter any number : "))
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a //= 10
    
# print(rev)

#4. ==================================================>
# a = int(input("Enter any number : "))

# copy = a
# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a //= 10
# if copy == rev:
#     print("Pallindrom")
# else:
#     print("Not pallindrome")

#5. ==================================================>

# import random
# num = random.randint(1, 10)

# tries = 0

# while True:
#     guess = int(input("Guess Your number btw 1 and 10 : "))

#     if num == guess:
#         tries += 1
#         print(f"You are right. You Guessed the number in {tries} tries")
#         break
#     elif num < guess:
#         print("Choose a little lower num")
#         tries += 1
#     elif num > guess:
#         print("Choose a little higher num")
#         tries += 1
#     else:
#         tries += 1
#         print("You are wrong")



"""Functions in python"""

# befor write any function we need to write "def" keyword and then write "function's name" then put "paranthesis" like "()".
#e.g.================>
# def hello():
#     print("This is a hello function so say hello world")

# hello()

# Parameters ==> The thing  you accept is parameter>
# Argument ==> The thing you provide to parameter is argument.>


# def sum(a, b):
#     print(f"The sum of yor numbers is {a + b}")

# sum(12, 34)

############ Default Argument or Keyword Argument====================================>
# def hello(name, age):
#     print(f"Your name i s{name} and age {age}")
    
# hello(age = 22, name = "Arjun")

############ Default Parameter ====================================>
# def sum(a, b=23):
#     print(f"Your sum is {a + b}")

# sum(23, 20)

# Question ======================================================>
def palindrome(str):
    rev = ""
    for i in range(len(str)-1 , -1, -1):
        rev = rev + str[i]
    
    if rev == str:
        print("Palindrome")
    else:
        print("Not a palindrome")
        
palindrome("naman")