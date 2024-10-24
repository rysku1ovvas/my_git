# i = 1
#
# while i < 5:
#     i += 1
#     print(i)
#
# def osnovnoy(func):
#     def word():
#         print("hello")
#         result = func()
#         print("Good bye")
#         return result
#     return word
#
# @osnovnoy
# def person():
#     print("My name is Ayana")
# person()
#
# def lesson(work):
#     def wrapper(*args):
#         print("Lesson starts")
#         res = work(*args)
#         print("Lesson finished")
#         return res
#     return wrapper
#
# @lesson
# def theme(name, surname):
#     print(f"Todays' lesson: Decorator. Teachers' name is {name} {surname}.")
#
# theme("Bahtiyar", "Jony")
#
# def osnovnoy(times):
#     def wrapper(func):
#         def work(*args):
#             for i in range(times):
#                 print("my name is Ayana.")
#                 result = func(*args)
#                 print(result)
#         return work
#     return wrapper
#
# @osnovnoy(3)
# def age(n):
#     print(f"{n} years old")
#
# age(18)

# def repeat(times):
#     def decorator(func):
#         def wrapper(*args):
#             for i in range(times):
#                 print(f"Вызов {i+1}:")
#                 result = func(*args)
#                 print(result)
#         return wrapper
#     return decorator
#
#
# @repeat(3)
# def greet(name):
#     return f"Привет, {name}!"
#
# greet("Akdil")



# def attack(func):
#     def wrapper(*args):
#         start()
#         attack_enemy()
#         result = func(*args)
#         end()
#         return result
#     return wrapper
#
# def start():
#     print("Начало хода персонажа.")
#
# def end():
#     print("Завершение хода.")

# def attack_enemy():
#     print(f"Атакует: {character_name}. Враг: {enemy_name}. Сила атаки: {damage}")
#
# @attack
# def log_turn(*args):
#     print(f"{enemy_name} получил {damage} урона.")
#
# character_name = input("Enter name: ")
# enemy_name = input("enter name enemy: ")
# damage = input("Сила атаки: ")
#
# log_turn(character_name, enemy_name, damage)
#
# def person(name, age, course):
#     print(f"имя {name} возраст {age} курс {course}")
# person("ayana", 18, "Python2")
#
# def person(name, age, course="okurmen"):
#     print(f"имя {name} возраст {age} курс {course}")
# person("ayana", 18)
#
# def person(name, age=18, course="okurmen"):
#     print(f"имя {name} возраст {age} курс {course}")
# person("ayana",23)
