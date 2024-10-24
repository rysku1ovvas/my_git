# from random import randint
# def find_num():                      #6
#     print("Угадай число в диапазоне 1 до 10")
#     while True:
#         number = randint(1, 10)
#         attempt = 0
#         while True:
#             attempt_input = int(input("Enter: "))
#             attempt += 1
#             if number > attempt_input:
#                 print("Введите число побольше:")
#             elif number < attempt_input:
#                 print("Введите число поменьше:")
#             elif number == attempt_input:
#                 print(f"Вы угадали число {number} за {attempt} попытки")
#                 break
#
#         play_again=input("Хотите поиграть еще раз? (да/нет): ")
#         if play_again.lower() != "да":
#             print("thank you")
#             break
#
# find_num()

# def find_num():
#     while True:
#         secret_number = randint(1, 10)
#         # print(secret_number)
#         attempt = 0
#
#         while True:
#             number = int(input("Введите число в диапазоне от 1 до 10: "))
#             attempt += 1
#
#             if number < secret_number:
#                 print("Ваше число меньше загаданного.")
#             elif number > secret_number:
#                 print("Ваше число больше загаданного.")
#             else:
#                 print(f"Вы угадали секретное число {secret_number} за {attempt} попыток!")
#                 break
#
#         play_again = input("Хотите сыграть еще раз? (да/нет): ")
#         if play_again.lower() != "да":
#             print("Спасибо за игру!")
#             break
# #
# find_num()

# import random
# students = ["Azamat", "Ainazik", "Ayana", "Nursultan", "Akdil", "Fatima", "Bibigul", "Kudaiberdi", "Zamirbek", "Mirbek", "Mederbek", "Talgarbek"]
# def find_by_name_student():
#     while True:
#         print("У вас есть 5 попыток.")
#         popitka = 5
#         target_student = random.choice(students)
#
#         while popitka != 0:
#             name = input("Введите имя студента: ").capitalize()
#
#             if name == target_student:
#                 print(f"{name} - это правильный ответ!")
#                 break
#             else:
#                 popitka -= 1
#                 print(f"Вы не угадали. Попробуйте еще раз. У вас осталось {popitka} попыток.")
#                 if popitka < 3:
#                     first_letter = target_student[0]
#                     print(f"Подсказка: первая буква: {first_letter}")
#
#         if popitka == 0:
#             print(f"Попытки закончились. Загаданное имя было: {target_student}")
#
#         answer = input("Желаете попробовать еще раз? (yes/no)\n")
#
#         while answer != "yes" and answer != "no":
#             answer = input("Некорректный ввод. Введите 'yes' или 'no':\n")
#
#         if answer == "no":
#             print(f"Спасибо за игру! Загаданное имя было: {target_student}")
#             break
# find_by_name_student()
#
#
# Asia = ["Kyrgyzstan", "Kazakstan", "Chine"]
# Europe = ["Russia", "Ukraine", "Italy"]
# America = ["USA", "Brazilian", "Canada"]
# Africa = ["Madagaskar", "Kenya", "Sudan"]
#
# import random
# def find_country():
#     popytka = 3
#     while True:
#         continent = int(input("Выберите материк (1 - Азия, 2 - Европа, 3 - Америка, 4 - Африка): "))
#         if continent == 1:
#             choice_country = random.choice(Asia)
#             print(choice_country)
#         elif continent == 2:
#             choice_country = random.choice(Europe)
#         elif continent == 3:
#             choice_country = random.choice(America)
#         elif continent == 4:
#             choice_country = random.choice(Africa)
#         else:
#             print("Выберите материк от 1 до 4")
#         print("Угадайту страну!")
#
#         while popytka > 0:
#             country = input("Введите название на английском: ").upper()
#             if country == choice_country:
#                 print("Вы выиграли!")
#                 break
#             else:
#                 popytka -= 1
#                 print("Повторите попытку")
#                 if popytka < 2:
#                     first_letter = choice_country[0]
#                     print(f"Подсказка! Первая буква {first_letter}")
#         if popytka == 0:
#             print(f"Вы не угадали страну! Загаданная страна была {choice_country}")
#             break
#
#
#         answer = input("Желаете попробовать еще раз? (yes/no)\n")
#
#         while answer != "yes" and answer != "no":
#             answer = input("Некорректный ввод. Введите 'yes' или 'no':\n")
#         if answer == "no":
#             print("Спасибо за игру!")
#             break
#
# find_country()


# find_by_name_student()

# words = ["pencil", "pen", "book", "copybook"]
#
# def find_word():
#     popytka = 5
#     while popytka > 0:
#         w = input("Введите слово: ").lower()
#         if w in words:
#             popytka -= 1
#             print(f"Вы угадали!")
#             break
#         else:
#             popytka -= 1
#             print("Слово отсутствует в списке. Повторите попытку!")
#     if popytka == 0:
#         print(f"У вас закончились попытки.Вот содержание списка {words}")
#
# find_word()

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
#     while True:
#         word, value = random.choice(list(animals.items()))
#         print("Игра началась. Угадайте животное!")
#         print(f"Подсказка: {value}")
#         attempts = 3
#         print(f"У вас есть {attempts} попыток на угадывание.")
#
#         while attempts != 0:
#             popytka = input("Введите ваше предположение: ").lower()
#             if popytka == word:
#                 print(f"Вы угадали!{word} - это правильный ответ.")
#                 break
#             else:
#                 attempts -= 1
#                 print(f"Неправильно. У вас осталось {attempts} попыток.")
#                 if attempts == 1:
#                     first_letter = word[0]
#                     print(f"Ещё одна подсказка! Первая буква: {first_letter}")
#         if attempts == 0:
#             print(f"Вы не угадали животное. Правильный ответ: {word}")
#
#         answer = input("Хотите поиграть ещё раз (да/нет): ")
#         while answer != "да" and answer != "нет":
#             answer = input("Некорректный ввод. Введите 'да' или 'нет':\n")
#         if answer == "no":
#             print("Спасибо за игру!")
#             break
# guess_animal_game()