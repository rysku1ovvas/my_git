#СПИСОК list()
# numbers = [2,4,7,4,7,8]     #1
# max_num = max(numbers)
# print(f"максимальное число: {max_num}")

# people = [
#     ["Tom", 29],
#     ["Alice", 33],
#     ["Bob", 27]
# ]
# for person in people:
#     for item in person:
#         print(item, end=" | ")

# people = [
#     ["Tom", 29],
#     ["Alice", 33],
#     ["Bob", 27]
# ]
# print(people[0])  # ["Tom", 29]
# print(people[0][0])  # Tom
# print(people[0][1])

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# people = [Person("Tom", 38), Person("Kate", 31), Person("Bob", 42),
#           Person("Alice", 34), Person("Sam", 25)]

# view = map(lambda p: p.name, people)
# for person in view:
#     print(person)

# def find_max_in_list(lst):
#     max_n = lst[0]
#     for n in lst:
#         if n > max_n:
#             max_n = n
#     return max_n
# lst = [4,7,6,9,5,4]
# print(find_max_in_list(lst))
#
# def remove_duplicates(lst):   #2
#     if not lst:
#         return None
# numbers = [ 1,2,3,5,"aya", 8]
# n = numbers.clear()
# print(numbers)

# numbers = [1,2,3,4,4,2,5]
# def remove_dublicates(lst):
#     return list(set(lst))
# new_numbers = remove_dublicates(numbers)
# print(new_numbers)

# def reverse_list(lst):          #3
#     return
# words = [1,2,3,"aya"]
# word = words.reverse()
# print(words)

# def sum_of_list(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#     return sum
# numbers = [1,4,3,6]
# n = sum_of_list(numbers)
# print(f"сумма всех чисел: {n}")

# def is_palindrome(lst):               #5
#     return lst == lst[::-1]
# print(is_palindrome([1,2,3,2,1]))


# word = "Hello"[1:4]
# print(word)

# def is_palindrome(lst):
#     return lst == reversed(lst)
# print(is_palindrome([1,2,3]))

# def double_of_list(lst):        #6
#     result = 1
#     for i in lst:
#         result *= i
#         print(f"double: {result}")
# numbers = [1,2,3,4,5]
# double_of_list(numbers)

# numbers = [1,2,3,4,5,6,7,8,9]           #7
# def condition(number):
#     return number % 2 != 0
# result = filter(condition, numbers)
# for n in result:
#     print(n)

# def odd(lst):
#     new_list = []
#     for i in lst:
#         if i % 2 != 0:
#             new_list.append(i)
#     return new_list
# lst = [1,2,3,4,5,6,7,8,9]
# print(odd(lst))

# def double(lst):
#     result = []
#     for x in lst():
#         result *= i
#         for y in range(1,11):
#
#     return
# lst = [1,2,3,4,5]

#
# numbers = [1,2,3,4,5,6,7,8,9]
# for i in numbers:
#     if i % 2 == 0:
#         print(f"Чётные числа: {i}")
#     else:
#         print(f"Нечётные числа: {i}")