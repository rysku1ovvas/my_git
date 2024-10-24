# names = ["Мирзабеков Азам = ИЯ(к)о-1-24","Назарбекова Карина = ИЯ(к)о-1-24","Камалова Лариса = ИЯ(к)о-1-24", "Бочорова Айзирек ИЯ(к)-1-24","Акимжанова Хадижа = ИЯ(к)о-1-24","Айсарова Райкан = ЭБ(к)-1-24","Мухамедова Хадижа = ЭБ(к)-1-24","Турдиева Раяна = ЭБ(к)-1-24","Махмудова Фатима  = ЭБ(к)-1-24","Мирланбекова Сундуз = ЭБ(к) -1-24","Нусыр Айша = ИЯ(к)о-3-24","Кудайбергенова Аль-Ирада = ИЯ(к)о-3-24","Адиева Нурсулу = ИЯ(к)о-3-24"]
# def sorted_names(names, start_letter, end_letter):
#     return [name for name in names if start_letter <= name[0] <= end_letter]
# name = sorted(names)
# result = sorted_names(names, "А", "Я")
# print(result, end="\n\t")
# from random import choice, random
# names = ("Мирзабеков Азам = ИЯ(к)о-1-24","Назарбекова Карина = ИЯ(к)о-1-24","Камалова Лариса = ИЯ(к)о-1-24", "Бочорова Айзирек ИЯ(к)-1-24","Акимжанова Хадижа = ИЯ(к)о-1-24","Айсарова Райкан = ЭБ(к)-1-24","Мухамедова Хадижа = ЭБ(к)-1-24","Турдиева Раяна = ЭБ(к)-1-24","Махмудова Фатима  = ЭБ(к)-1-24","Мирланбекова Сундуз = ЭБ(к) -1-24","Нусыр Айша = ИЯ(к)о-3-24","Кудайбергенова Аль-Ирада = ИЯ(к)о-3-24","Адиева Нурсулу = ИЯ(к)о-3-24")
# sorted_names = sorted(names)
# print(sorted_names, end="\n")


# def filter_by_length(strings, min_length):           #1
#     new_strings = []
#     for i in strings:
#         if len(i) >= min_length:
#             new_strings.append(i)
#     return new_strings
#
# strings = ["Ayana", "Ayan", "Ainazik", "Akdil", "Mirbek"]
# min_length = 5
# filtered_strings = filter_by_length(strings, min_length)
# print(filtered_strings)

# def contains_substring(strings, substring):        #2
#     return strings + substring
# strings = ["ayana", "ayan"]
# substring = ["Hello"]
# new_string = contains_substring(strings, substring)
# print(new_string)

# def capitalize_if_starts_with(strings, letter):              #3
#     new_strings = []
#     for i in strings:
#         if i.startswith(letter):
#             new_strings.append(i.capitalize())
#         else:
#             new_strings.append(i)
#     return new_strings
# strings = ["ayan", "ainaz", "nurik", "sake"]
# letter = "a"
# new_strings = capitalize_if_starts_with(strings, letter)
# print(new_strings)




