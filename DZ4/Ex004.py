# Задача 1. Вычислить результат деления двух чисел c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

#Раз задача не обязательна, то я решил написать калькулятор c вводом точности исчисления:

# n1 = float(input("Введите первое число:"))
# n2 = float(input("Введите второе число:"))
# print("+ сложение")
# print("- вычитание")
# print("* умножение")
# print("/ деление")
# b = str(input('Какую операцию выполнить?:'))
# d = str(input('Укажите точность вычисления (от 0.1 до бесконечности цифр после запятой): '))

# def Calculator(n1,n2,b,d):
#     spisok = list(d)
#     i = 0
#     for e in spisok:
#         i+=1
#     i = i-2

#     x = 0
#     o = False
#     while o == False:
#         if b == '+' or b == 'сложить' or b == 'сложение':
#             x = n1+n2
#             o = True
#         if b == '-' or b == 'вычесть' or b == 'вычетание':
#             x = n1-n1
#             o = True
#         if b == '*' or b == 'умножить' or b == 'умножение':
#             x = n1*n2
#             o = True
#         if b == '/' or b == 'делить' or b == 'деление':
#             x = n1/n2
#             o = True
#         else:
#             print("Операция не распознана.")
#             b = str(input('Какую операцию выполнить?:'))
#     print(round(x, i))

# Calculator(n1,n2,b,d)

#Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Задайте натуральное число: '))

# def Prime_Factors(n):
#     spisok_rez = []
#     for e in range(2, n):
#         if n%e == 0:
#             spisok_rez.append(e)
#         else:
#             continue
#     return spisok_rez

# print(Prime_Factors(n))


# Задача 3. (необязательное). Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча
#  и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков

# Конкретный пример ввода-вывода приведён ниже.

# Порядок вывода команд произвольный.

# Sample Input:

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

# Оно не работает

# n = int(input('Введите количество игр: '))
# teams = str(input('Введите названия команд через пробел: '))
# spisok_teams = []

# element = ''
# for e in teams:
#     element += e
#     if e == ' ':
#         spisok_teams.append(element)
#         element = ''
# spisok_teams.append(element)
# print(spisok_teams)

# rez = []
# i = 0
# for e in spisok_teams:
#     print('Введите результат матчей для команды', e, ':')
#     i = int(input())
#     rez.append(i)
# i = 0
# spisok_rez = []
# for e in spisok_teams:
#     spisok_rez.append(e)
#     spisok_rez.append(rez[i])
#     i+=1
# print(spisok_rez)

# spisok_final = []
# win = 0
# draw = 0
# loss = 0
# i = 0
# for e in spisok_teams:
#     if e != int():
#         spisok_final.append(e)
#     if e == int():
#         for j in rez:
#             if j > e:
#                 win += 1
#             elif j == e:
#                 draw += 1
#             elif j < e:
#                 loss += 1
#             i += 1
#     spisok_final.append(i)
#     spisok_final.append(win)
#     spisok_final.append(draw)
#     spisok_final.append(loss)
#     print(spisok_final)
#     i = 0
#     win = 0
#     draw = 0
#     loss = 0
#     spisok_final = []

    # Забыл добавить элемент который будет считать колличество очков.