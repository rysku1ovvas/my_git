# class Solution:
#     def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
#
#         target = {}
#         for targetWord in words2:
#             toAdd = {}
#             for letter in targetWord:
#                 if letter not in toAdd:
#                     toAdd[letter] = 1
#                 else:
#                     toAdd[letter] += 1
#
#             for letter, occur in toAdd.items():
#                 if letter in target:
#                     target[letter] = max(occur, target[letter])
#                 else:
#                     target[letter] = occur
#
#         ret = []
#         for a in words1:
#             toInclude = True
#             for key in target:
#                 if a.count(key) < target[key]:
#                     toInclude = False
#                     break
#             if toInclude:
#                 ret.append(a)
#         return ret

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# n = [i for i in a if i < 5]
# print(n)
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# new = [i for i in a if i in b]
# print(new)

#
# # num = int(input("enter F: "))
# def farengeit (celsius):
#     return (celsius * 9/5) + 32
# def celcius (fahrenheit):
#     return (fahrenheit - 32) * 5/9

# # farengeit()
# celcius(25)

def celsius_for_farenhate(celsius):
    return (celsius * 9/5) + 32
def farenhate_for_celsius(farenhate):
    return (farenhate - 32) *5/9

print("Преобразование температу: "
      "1-Цельсий в Фаренгейт;"
      "2- Фаренгейт в Цельсий.")
def main():
    choice = int(input("enter 1 or 2: "))
    if choice == 1:
        celsius = float(input("enter C: "))
        farenhate = celsius_for_farenhate(celsius)
        print(f"Температура в Фаренгейте:{farenhate}")
    elif choice == 2:
        farenhate = float(input("enter F: "))
        celsius = farenhate_for_celsius(farenhate)
        print(f"Температура в Цельсие:{celsius}")
    else:
        print("Неправильно. Выберите или 1 или 2!!!")
main()