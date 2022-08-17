#Задача 1. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
# например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55
# то в итоге будет, 3*x^3 + 12*x^2+10*x+66

# Создал файлы с полиномами
# from fileinput import close
# import json
# import random

# n1 = int(input('Введите колличество членов первого многочлена:'))
# n2 = int(input('Введите колличество членов второго многочлена:'))

# n1 -=1
# n2 -=1

# # Создаём полином.

# def Add_Polynom(n): 
#     spisok = []
#     stepen = n
#     i = 0
#     while i < n:
#         rnd = int(random.randint(2, 20))
#         if stepen > 1:
#             spisok.append(int(rnd))
#             spisok.append(f'x^{stepen}')
#             spisok.append('+')
#         elif stepen == 1:
#             spisok.append(int(rnd))
#             spisok.append(f'x')
#             spisok.append('+')
#         i+=1
#         stepen-=1
#     spisok.append(int(rnd))
#     return spisok

# # Используем функцию для создания двух полиномов.

# polynom1 = Add_Polynom(n1)
# Add_Polynom(n2)
# polynom2 = Add_Polynom(n2)

# print(polynom1)
# print(polynom2)

# # Загружаем полиномы в файлы.

# def Upload_Files(polynom1,polynom2):
#     print('Запись файлов.')

#     with open('polynom1.json', 'w', encoding = 'utf-8') as fh:
#         fh.write(json.dumps(polynom1, ensure_ascii= False))
#     print('Файл 1 записан: polynom1.json')

#     with open('polynom2.json', 'w', encoding = 'utf-8') as fh:
#         fh.write(json.dumps(polynom2, ensure_ascii= False))
#     print('Файл 2 записан: polynom2.json')

# Upload_Files(polynom1,polynom2)

# # Считываем с файлов информацию.

# print('Чтение файлов:')

# def File_Read1(spisok1):
#     with open('polynom1.json', 'r', encoding = 'utf-8') as fh:
#         spisok1 = list(json.load(fh))
    
#     return spisok1

# def File_Read2(spisok2):
#     with open('polynom2.json', 'r', encoding = 'utf-8') as fh:
#         spisok2 = list(json.load(fh))
    
#     return spisok2

# spisok1 = File_Read1(polynom1)
# spisok2 = File_Read2(polynom2)


# print(f'Файл 1:,{spisok1}')
# print(f'Файл 2:,{spisok2}')

# spisok_reverseve = []
# spisok1.reverse()
# spisok2.reverse()
# spisok_result = []

# if len(spisok1) > len(spisok2):
#     spisok_reversive = spisok1
# else:
#     spisok_reversive = spisok2
# temp = 0
# i = 0
# for e in spisok_reversive:
#     if i < len(spisok2):
#         if e in range(0, 100):
#             spisok_result.append(e + spisok2[i])
#         else:
#             spisok_result.append(e)
#         i+=1
#     else:
#         spisok_result.append(e)
        
# spisok_result.reverse()
# print()
# print(spisok_result)

# def Upload_File_Result(spisok_result):
#     print('Запись файла.')

#     with open('polynom_result.json', 'w', encoding = 'utf-8') as fh:
#         fh.write(json.dumps(spisok_result, ensure_ascii= False))
#     print('Файл записан: polynom_result.json')
# Upload_File_Result(spisok_result)



#Задача 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]


# spisok = [1, 3, 5, 2, 4, 4, 7]
# print(f'Ищем последовательность в этом списке: {spisok}')

# def Sequence_Search(spisok):
#     spisok2 = spisok
#     spisok_search = []

#     for e in spisok:
#         for i in spisok2:
#             if i == e+1:
#                 spisok_search.append(e)
#                 spisok_search.append(i)
#     spisok_result = []
#     spisok_result.append(min(spisok_search))
#     spisok_result.append(max(spisok_search))
#     return f'Последовательность найдена: {spisok_result}'
# print(Sequence_Search(spisok))


#Задача 3. (необязательная) Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

