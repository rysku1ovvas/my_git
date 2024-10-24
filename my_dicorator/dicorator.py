# def my_decorator(function):  #основная функция
#     def wrapper():         #Вложенная функция
#         print("Hello!")
#         result = function()
#         print("Ayan")
#         return result
#     return wrapper

# @my_decorator
# def my_func():
#     print("my function")
# my_func()
#
# m = my_decorator(my_func)
# m()

# def decorator(aya):
#     def word():
#         print("Старт основной функции!")
#         result = aya()
#         print("Конец")
#         return result
#     return word
# @decorator
# def func():
#     print("My name's Ayana")
#
# func()

# def osnovnoi_function(function):
#     def vnutrenniy():
#         print("Регистрация")
#         print("Логин")
#         resultat = function()
#         print("Выход")
#         return resultat
#     return vnutrenniy
# @osnovnoi_function
# def sbros():
#     print("Добавить картинку")
# sbros()

# def decorator(game):
#     def d_game():
#         start_game()
#         num()
#         result = game()
#         stop_game()
#         return result
#     return d_game
#
# def num():
#     print("Очко")
#
# @decorator
# def level_up():
#     print("Уровень повышен")
#
# @decorator
# def level_down():
#     print("Уровень понижен")
#
# def start_game():
#     print("start game")
# def stop_game():
#     print("stop")
#
# level_up()
# level_down()


# def osnovnoy(work):
#     def vnutrenniy():
#         start_session()
#         resultat = work()
#         finished_session()
#         return resultat
#     return vnutrenniy
#
# @osnovnoy
# def tovar():
#     print("Добавить товар в корзинку")
#
# @osnovnoy
# def log_out():
#     print("log out")
#
# @osnovnoy
# def pay():
#     print("Оплата за товар")
#
# @osnovnoy
# def see():
#     print("Смотреть где едет товар")
#
# def start_session():
#     print("start")
# def finished_session():
#     print("stop")
#
# tovar()
# log_out()
# pay()


# import time
# def measure_time(function):
#     def wrapper():
#         start = time.time()
#         res = function()
#         end = time.time()
#         work = end - start
#         print(f"Время выполнения работы: {work}")
#         return res
#     return wrapper
# @measure_time
# def example():
#     time.sleep(15)
# ayan = example()
# print(ayan)
#
# def calculator(function):
#     def operation(*args):
#         start()
#         res = function(*args)
#         end()
#         return res
#     return operation
# def start():
#     print("Начало работы калькулятора.")
#
# def end():
#     print("Конец работы калькулятора.")
#
# @calculator
# def add(a,b):
#     # a = int(input("enter number"))
#     # b = int(input("enter second number"))
#     print(f"{a} + {b} = {a + b}")
#
# @calculator
# def subtract(a, b):
#     if a > b:
#         print(a)
#     elif a < b:
#         print(b)
#     else:
#         print(f"{a} = {b}")
#
# @calculator
# def multiply(a, b):
#     print(F"{a} * {b} = {a * b}")
#
# @calculator
# def divide(a, b):
#     if a == 0 or b == 0:
#         print("На ноль делить нельзя!")
#     else:
#         print(f"{a} / {b} = {a/b}")
#
# add(1,2)
# subtract(2,3)
# multiply(4,2)
# divide(6,0)

# def order_notification(work):
#     def wrapper():
#         start()
#         res = work()
#         end()
#         return res
#     return wrapper
#
# def start():
#     print("Начало обработки заказа...")
#
# def end():
#     print("Конец обработки заказа.")
#
# @order_notification
# def create_order():
#     name = input("enter name: ")
#     print("1-home")
#     print("2-garden")
#     print("3-beauty")
#     print("4-clothes")
#     thing = int(input("choose tovar: "))
#     print(f"Заказ оформлен: {name} {thing}")
# create_order()

def repeat(times):
    def decorator(func):
        def wrapper(*args):
            for i in range(times):
                print(f"Вызов {i+1}:")
                result = func(*args)
                print(result)
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    return f"Привет, {name}!"

greet("Akdil")