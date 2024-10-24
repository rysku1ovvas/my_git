# people = {"Ayana", "Ainaz", "Akdil", "Bahtiyar"}
# a, _, c, _ = people
# print(a)

# a, b, c, d = people
# print(a)
# print(b)
# print(c)
# print(d)

# str = ("Ayana")
# a,b,c,d,e = str
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# _, *b, _ = str
# print(b)

# *_, last = str
# print(_)
# print(last)

# num1 = [1,2,3,4,5]
# num2 = [6,7,8,9]
# if len(num1) == len(num2):
#     num3 = [*num1, *num2]
#     print(num3)
# else:
#     print("Кошулбайт")


a = 10
b = 20
a, b = b, a
print(a)
print(b)

mixed_list = [1, "Hello", (10, 20), [30, 40]]
integer, string, tuple_values, list_values = mixed_list
print(integer)

def print_coordinates(x, y, z):
    print(f"X: {x}, Y: {y}, Z: {z}")

coordinates = [10, 20, 30]
print_coordinates(*coordinates)

data = [[10, 20], [30, 40], [50, 60]]
for inner_list in data:
    x, y = inner_list
    print(x, y)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_three, *middle, last_two = data
print(first_three)

data = [7, 14, 21, 28]
a, b, c, d = [value // 7 for value in data]
print(a, b, c, d)


list1 = [100, 200]
list2 = [300, 400, 500, 600]
first_elements = [list1[0], list2[0]]
tail_elements = list1[1:] + list2[1:]
print(first_elements)
print(tail_elements)