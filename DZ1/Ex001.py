#Задача 1: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

n = int(input('Введите номер дня недели: '))

def WeekendDay(a):
    if n>5 and n<8:
        print('День выходной.')
    elif n>0 and n<6:
        print('День будний.')
    else:
        print('Нет такого дня недели.')
WeekendDay(n)

#======================================================

#Задача 3: Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x =int(input('Введите координату Х: '))
y =int(input('Введите координату Y: '))

def Chetvert(x,y):
    if x<0 and y>0:
        print('Первая четверть.')
    elif x>0 and y>0:
        print('Вторая четверть.')
    elif x<0 and y<0:
        print('Третья четверть.')
    elif x>0 and y<0:
        print('Четвёртая четверть.')
    else:
        print('Четверть не найдена.')
Chetvert(x,y)