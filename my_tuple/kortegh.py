# nums = (1,2,3,4,5,6,7,8,9)
# max_num = max(nums)
# min_num = min(nums)
# print(f"Максимальное число :{max_num}")
# print(f"Минимальное число :{min_num}")

# max_num = nums[0]
# min_num = nums[0]
# for i in nums:
#     if i > max_num:
#         max_num = i
#     if i < min_num:
#         min_num = i
# print(f"Максимальное число : {max_num}")
# print(f"Минимальное число : {min_num}")

# python_2 = ("Ayana", "Ainazik", "Fatima", "Meder", "Akdil", "Mirbek", "Zamirbek")
# for person in python_2:
#     if len(person) > 6:
#         person = python_2
# for name in python_2:
#     if name.startswith("A"):
#
#
# print(person)
# print(name)

# cities = ["Almaty", "Marocco", "Madina", "Bishkek", "Mekke"]
# new = [i for i in cities if i.startswith("M")]
# print(new)
#
# people = ("Ayana", "Ainazik", "Fatima", "Meder", "Akdil", "Mirbek", "Zamirbek")
# person = tuple(i for i in people if len(i) > 6)
# print(person)
#
# new = [i for i in people if i.startswith("A")]
# print(new)
#
# numbers = (4, 7, 8, 2, 5, 8, 9)
# n = numbers.index(8)
# print(n)
#
# letters = ('a', 'b', 'c', 'a', 'd', 'a', 'e')
# l = letters.count('a')
# print(l)
#
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# new = tuple(tuple1 + tuple2)
# print(new)
# print(tuple(new))
#
# tuple1 = (1, 2, 3)
# tuple2 = (1, 2, 3)
# if tuple1 == tuple2:
#     print(f"{tuple1} равна {tuple2}")
# else:
#     print(f"{tuple1} не равна {tuple2}")
#
# string = "hello"
# new = tuple(string)
# print(new)
#
# tuple1 = (1, 3, 5)
# tuple2 = (2, 4, 6)
# res = tuple(tuple1[0:2:2] + tuple2[0:2:2] + tuple1[1:2] + tuple2[1:2] + tuple1[-1:] + tuple2[-1:])
# print(res)
#
# num = (1,3,2,5,4,7,6,9,8)
# num2 = (9,8,7,6,5,4,3,2,1)
#
# def sum(tuple1, tuple2):
#     if len(tuple1) != len(tuple2):
#         return "Длина кортежей не равна"
#
#     res = []
#     for i in range(len(tuple1)):
#         res.append(tuple1[i] + tuple2[i])
#     return tuple(res)
#
# tuple1 = (1, 10, 34)
# tuple2 = (9, 35, 57)
# res = sum(tuple1, tuple2)
# print(res)
