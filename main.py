#ФУНКЦИЯ def
# def multiple(number):
#     if number % 2 == 0:
#         print(number ** 2)
#
# multiple(4)
#
# def calculate(number , number2):   #1-вычисление
#     print(number + number2)
#     print(number - number2)
#     print(number / number2)
#     print(number % number2)

# n1 = int(input("enter number: "))
# n2 = int(input("enter number: "))
# print(n1 + n2)
# print(n1 - n2)
# print(n1 / n2)
# print(n1 % n2)

# if 0:
#      print("True")
# else:
#      print("False")

# calculate(6,2)

# def comparison(number,number2):  #2-наименьшее
#     if number < number2:
#         print(number)
#     elif number > number2:
#         print(number2)
#     else:
#         number == number2
#         print("числа равны")
# n= int(input("enter number:"))
# n2 = int(input("enter second number:"))
# comparison(n,n2)

# def dlina(word):   #3-длина
#     word_len = len(word)
#     print(word_len)
# w = input("enter word: ")
# dlina(w)

# def calculate(number , number2, number3): #4-сумма
#     print(number + number2 + number3)
# n = int(input("enter: "))
# n2 = int(input("enter: "))
# n3 = int(input("enter: "))
# calculate(n , n2 , n3)
#
# def kvadrat(number):   #5-квадрат
#     print(number**2)
# kvadrat(9)
#
# def sum_up_to(num):  #6-сумма чисел от 1 до n включая
#     n = 0
#     for i in range(1, num+1):
#         n += i
#     print(n)
#
# sum_up_to(4)
#
# def factorial(n):  #7-факториал
#     num = 1
#     i = 1
#     while i <= n:
#         num *= i
#         i += 1
#         print(num)
#
# factorial(9)

# def word_and_symbol(word, symbol):  #9-наличие символа в слове
#     if symbol in word:
#         print("TRUE")
#     else:
#         print("FALSE")
# word_and_symbol("ayana", "n")

# def count_symbol(word, symbol):   #10-сколько
#     if symbol in word:
#         c = word.count(s)
#     print(c)
# w = input("enter: ")
# s = input("enter: ")
# print()
# count_symbol(w,s)
# def word_and_symbol("aya" , 3):

# def word_and_symbol(word,symbol):
#     while symbol >= 0:
#         print(word*symbol)
#
# word_and_symbol("ayana", 3)

# def greet(name):
#     print(f"Привет, {name}!")
# greet("Ayana")


# n = input("enter:")
# n2 = input("enter:")
# n3 = input("enter:")
# n4 = input("enter:")
# n5 = input("enter:")
# list = (n, n2, n3, n4, n5)
# print(list)

# def word_and_symbol(word , symbol):
#     n = 0
#     for i in range(len(word)):
#         n += i
#         print(n)
# word_and_symbol("ayana", 3)

# def numbers(num1, num2):
#     return num1 % num2 == 0
#
# # res = numbers(4,3)
# print(numbers(8,2))

# def numbers(*numbers):
#     for i in numbers:
#
#         if numbers <= 50:
#             print(numbers)
#         else:
#             print(numbers ** 2)
#     # return numbers ** 3 > 50
# print(numbers( 10, 5, 55, 80))

# def num(*numbers):
#     if numbers < 50:
#         print(num)
# print(num(3,10,50))

# def say_hello():
#     print("hello")
# say_hello()

# def print_messages():
#     def say_hello():
#         print("Hello")
#     def say_goodbye():
#         print("Good Bye")
#     say_hello()
#     say_goodbye()
# print_messages()

# def main():
#     say_hello()
#     say_goodbye()
# def say_goodbye():
#     print("good")
# def say_hello():
#     print("hello")
# main()

# def name_and_age(name, age):
#     print(f"Name : {name}")
#     print(f"Age : {age}")
#
# name_and_age("Ayana", 18)

# def sum(*numbers):
#     result = 0
#     for i in numbers:
#         result += i
#     print(f"sum: {result}")
# sum(1,4,8,7,3)

# def mess():
#     return "hi Ayana"
# # print(mess())
# get = mess()
# print(get)

# def double(num):
#     return 2 * num
# # print(double(3))
# result = double(5)
# print(f" double : {result}")

# def sum(a, b):
#     return a + b
# print(sum(3,8))
# res_sum = sum(2,5)
# print(res_sum)

# def person(name, age):
#     print(f"Name: {name}  Age: {age}")
#     if age >= 18:
#         print("подросток")
#         return
#     # print(f"{name}")
# person("Ayana", 18)

# def table_of_three(number):             #1-кобойтунду
#     for i in range(1, 10 + 1):
#         print(f"{number} * {i} = {number * i}")
# table_of_three(4)

# def sum(n):          #2
#     res = 0
#     number = 1
#     while number <= n:
#         res += number
#         number += 1
#     return res
# print(sum(4))

# def find_max(num1, num2, num3):            #3
#     if num2 < num1 > num3:
#         print(f"Наибольшее число: {num1}")
#     elif num1 < num2 > num3:
#         print(f"Наибольшее число: {num2}")
#     else:
#         num1 < num3 > num2
#         print(f"Наибольшее число: {num3}")
# find_max( 1, 4, 9)

# def nums(*numbers):              #4
#     n = 1
#     for i in numbers:
#         n *= i
#         print(f"Произведение всех чисел: {n}")
# nums(1,4,3,4,2)

# def find_max(*numbers):               #5
#     n = numbers[0]
#     for number in numbers[1:]:
#         if number > n:
#             n = number
#     return n
# print(find_max(1,4,2,9,5))
