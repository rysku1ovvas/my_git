# groupmates = {"Ryskulova" : "Ayana" , "Kydykbaev" : "Akdil" , "Abdyjapar kyzy": "Ainazik"}
# print(groupmates["Ryskulova"])
from operator import invert

# for value in groupmates.values():
#     print(value)

# for key in groupmates.keys():
#     print(key)

# fruits = {"apple" : "4" , "banana" : 7 , "oranges" : 6}
# print(fruits["apple"])
#
# for value in fruits.values():
#     if value <= 3:
#         value += 3
#         print(value)
#     else:
#         value -= 1
#         print(value)
#

# my_dict = {}
# names = {"name" : "Ayana", "name2" : "ayana", "name3" : "Ayan"}
# my_dict.update(names)
# print(my_dict)
#
# fruits = {"apple" : 4 , "banana" : 7 , "oranges" : 6}
# print(fruits["apple"])
#
# person = {"name": "Alice", "age": 30, "city": "New York"}
# print(person["age"])
# #
# for value in fruits.values():
#     if value == 7:
#         print(value + 2)

# if "apple" in fruits:
#     print(True)
# else:
#     print(False)
# print(bool if "apple" in fruits)
#
# print(person.keys())
#
# print(fruits.values())
#
# print(person.items())
#
# del fruits["oranges"]
# print(fruits)
#
# print(my_dict.clear())


# invert_dict={"n1" : 19 , "n2": 28, "n3": 86}
# new_dict = {value: key for key, value in invert_dict.items()}
# print(new_dict)


# def dict_to_tuple_list(n):
#     print(list(n.items()))
# ages = {'Akdil': 25, 'Fatima': 30, 'Mirbek': 35}
# tuple_ages = dict_to_tuple_list(ages)
# print(tuple_ages)
#
# grades = {
#     'Аяна': 96, 'Акдил': 89, 'Талгарбек': 75, 'Бибигул': 69,
#     'Мирбек': 89, 'Айназик': 81, 'Медербек': 80, 'Кудайберди': 86,
#     'Фатима': 84, 'Замирбек': 91, 'Азамат': 13
# }
#
# def dictionary():
#     passed_items = {}
#     nopassed_dict = {}
#     for key, value in grades.items():
#         if value >= 80:
#             passed_items[key] = value
#         else:
#             nopassed_dict[key] = value
#     return f"Прошли {passed_items} \nНе прошли {nopassed_dict}"
#
# print(dictionary())

# text = "Менин менин атым атым Аяна аяна "
# def func(text):
#     a = text.lower().split()
#     repeated_words = {}
#     for i in a:
#         if i in repeated_words:
#             repeated_words[i] += 1
#         else:
#             repeated_words[i] = 1
#     return repeated_words
# print(func(text))

# list = [1,2,3,4,5]
# def func(list):
#     dict = {}
#     for i in list:
#         dict[i] = i * i
#     return dict
# print(func(list))

# функция эки словарь бириктирип если ключи окшош значениялары кошулат

# dict1 = {"apple" : 3, "banana" : 5, "grape" : 2}
# dict2 = {"orange" : 5, "grape" : 6}

# def ayan():
#     new_dict = {}
#     for i in new_dict:
#         if i in dict1 == dict2:
#             new_dict[i] = i + i
#         else:
#             new_dict[i] = i
#     return new_dict
#
#
# print(ayan())

# import random
# animals = {
# 'слон': 'Это самое большое наземное животное.',
# 'тигр': 'Это полосатый хищник.',
# 'панда': 'Это черно-белое животное, которое ест бамбук.',
# 'крокодил': 'Это рептилия, которая живет в воде.',
# 'коала': 'Это сумчатое животное, которое обитает в Австралии.',
# }
#
# def guess_animal_game():
#     animal, ayan = random.choice(list(animals.items()))
#
#     print("Угадайте животное!")
#     print(f"Подсказка: {ayan}")
#
#     person = input("Введите ваше предположение: ").lower()
#
#     if person == animal:
#         print("Вы угадали!")
#     else:
#         print(f"Вы не угадали. Правильный ответ: {animal}")
#
# guess_animal_game()

