# Задача 1: Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# n = str(input('Введите число или цифру для поиска: '))
# spisok = ["qw23e", "asd", "123", "q1we", "ertqwe"]

# def Number_Search(n):
#     number = 0
#     temp = bool
#     for i in spisok:
#         if i == n:
#             temp == True
#             print('В списке присутствует число "', n, '" в ', number,'строке.')      # поиск числа в списке строк
#             print('Вывод строки: ', spisok[number])
#         for j in i:
#             if j == n:
#                 temp = True
#                 print('В списке присутствует число "', n, '" в ', number,'строке.')  # поиск конкретной цифры в строке
#                 print('Вывод строки: ', spisok[number])
#             else: 
#                 continue
#         number += 1
#         if temp == False:
#             print('В списке не присутствует число "', n, '".')
# print(Number_Search(n))

# =====================================================================================================================
# =====================================================================================================================

# Задача 2: Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# n = str(input('Введите строку для поиска повторных вхождений: '))
# spisok = ["qw23e","qwer", "123", "zxc", "qwer", "q1we", "123"]
# def Second_Occurrence(n,spisok):
#     i = 0
#     number = 0
#     for e in spisok:
#         if e == n:
#             number = i
#         i += 1
#     if number > 1:
#         print('Второе вхождение строка №', number)
#     else:
#         print('Второе вхождение не обнаружено.')
# Second_Occurrence(n,spisok)

# =====================================================================================================================
# =====================================================================================================================


# 3* (необзательная).
# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.

# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений 
# (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.