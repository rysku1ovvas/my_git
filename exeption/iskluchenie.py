# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     print("Результат деления:", number1/number2)
#     my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print(my_list[10])
# except ValueError:
#     print("Преобразование прошло неудачно")
# except ZeroDivisionError:
#     print("Попытка деления числа на ноль")
# except BaseException:
#     print("Общее исключение")
# finally:
#     print("Блок try завершил выполнение")


# try:
#     num1 = int(input("enter number: "))
#     num2 = int(input("enter second number: "))
#     print("result: ", num1 / num2)
#
# except ZeroDivisionError as e:
#     print("На ноль делить нельзя", e)
#
# except ValueError as e:
#     print("Преобразение невозможно", e)
#
# finally:
#     print("Программа завершена")

# numbers = input("Введите список чисел, разделенных пробелами: ").split()
# print(numbers)
#
# num = 0
# for i in numbers:
#     try:
#         num += int(i)
#
#     except ValueError as e:
#         print("Ошибка", e)
#
# print("sum of numbers:", num)

# try:
#     num1 = int(input("enter number: "))
#     num2 = int(input("enter second number: "))
#     print("first list of numbers: ", num1)
#
#     try:
#         print("Деление of numbers: ", num1 / num2)
#     except ZeroDivisionError as e:
#         print("На ноль делить нельзя", e)
# except ValueError as e:
#     print("Ошибка", e)
# finally:
#     print("Программа завершила свою работу")

#
# def check_password_strength(password):
#     if len(password) < 8:
#         raise ValueError("Пароль должен содержать не менее 8 символов.")
#
#     if not any(i.isdigit() for i in password):
#         raise ValueError("Пароль должен содержать хотя бы одну цифру.")
#
#     if not any(i.islower() for i in password):
#         raise ValueError("Пароль должен содержать хотя бы одну букву в нижнем регистре.")
#
#     if not any(i.isupper() for i in password):
#         raise ValueError("Пароль должен содержать хотя бы одну букву в верхнем регистре.")
#
#     return "Пароль достаточно надёжный."
#
# while True:
#     try:
#         password = input("Введите пароль: ")
#         result = check_password_strength(password)
#         print(result)
#         break
#     except ValueError as e:
#         print(f"Ошибка: ", e)
#     finally:
#         print("Проверка пароля завершена.")



# users = {
# "admin": "admin123",
# "user1": "pass123",
# "guest": "guestpass",
# }
# def login(name, password):
#     if name in users and users[name] == password:
#         return True
#     else:
#         raise ValueError("Неверный пароль или логин.")
# while True:
#     try:
#         name = input("Введите логин: ")
#         password = input("Введите пароль: ")
#         if login(name, password):
#             print("Вы успешно вошли в систему!")
#             break
#     except ValueError as e:
#         print(e)
#     finally:
#         print("Проверка данных завершена.")



shop = {
"меч": 100,
"щит": 150,
"зелье": 50,
}
balance = 300
def buy_item(item, quantity, balance):
    try:
        if item not in shop:
            raise ValueError("Товар не найден в магазине.")

        total_cost = shop[item] * quantity

        if total_cost > balance:
            raise ValueError("Недостаточно денег для покупки.")

        balance -= total_cost
        print(f"Вы купили {quantity} шт. '{item}' за {total_cost} монет. Остаток {balance} монет.")
        return balance
    except ValueError as e:
        print("Ошибка: ", e)

    finally:
        print("Спасибо за посещение нашего магазина!")


#
buy_item("меч", 5, balance)
buy_item("щит", 2, balance)
buy_item("зелье", 2, balance)

# def get_student_data(name, age, phone):
#     if not name.isalpha():
#         raise ValueError("Ошибка.Имя должно состоять только из алфавитных символов.")
#     if not str(age).isdigit():
#         raise ValueError("Возраст должен состоять из цифр.")
#     if not str(phone).isdigit():
#         raise ValueError("Номер телефона должен состоять только из цифр.")
#     return "Данные успешно сохранены."
# while True:
#     try:
#         name = input("Введите имя: ")
#         age = int(input("Введите возраст: "))
#         phone = input("Введите номер телефона: ")
#         print(f"Имя: {name}. Возраст: {age}. Номер телефона: {phone}")
#         result = get_student_data(name, age, phone)
#         print(result)
#         break
#     except ValueError as e:
#         print(e)
#     finally:
#         print("Регистрация прошла успешно.")


# def get_student_data(name, age, phone):
    # Проверка на наличие только букв в имени
#     if not name.isalpha():
#         raise ValueError("Имя должно состоять только из алфавитных символов.")
#
#     # Проверка на числовое значение возраста
#     if not str(age).isdigit() or age <= 0:
#         raise ValueError("Возраст должен быть положительным числом.")
#
#     # Проверка на числовое значение номера телефона
#     if not str(phone).isdigit() :
#         raise ValueError("Номер телефона должен состоять только из цифр.")
#
#     return "Данные успешно сохранены."
#
#
# while True:
#     try:
#         name = input("Введите имя: ")
#         age = int(input("Введите возраст: "))
#         phone = input("Введите номер телефона: ")
#
#         # Вызов функции для проверки и сохранения данных
#         result = get_student_data(name, age, phone)
#         print(result)
#         break  # Выход из цикла при успешной регистрации
#
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#
#     finally:
#         print("Попытка регистрации завершена.")

