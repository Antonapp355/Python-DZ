n = str(input('Введите пример: '))
spisok = list(map(str,n))
spisok_operation = []
spisok_position_operation = []
spisok_numbers = []
temp = ''
i = 0
for e in spisok:                                        # ищем знаки операций и узнаём их позиции (11+33+2 ==> ['1','1','+','3','3','+','2'] ==> 2,5)
    if e == '+' or e == '-' or e == '*' or e == '/':
        spisok_position_operation.append(i)             # Позиция знака +,-,*,/
        spisok_operation.append(e)                      # Знак операции +,-,*,/
    i += 1


print(f'spisok_position_operation: {spisok_position_operation}')
spisok_position_operation.append(i)                     # Добавляю доп элемент чтобы в будущем хватило индекса
print(f'spisok_operation: {spisok_operation}')
spisok_operation.append(i)                              # Добавляю доп элемент операции в список, чтобы отсчитывать числа до элемента операции

i = 0
j = 0
while j < len(spisok_position_operation):               # Определяем числа по позиции знака операции
    while i < spisok_position_operation[j]:
        temp = temp + spisok[i]                         # Для начала записываем число в переменную (по одной цифре: '1','2'==> '12')
        i+=1
    i+=1
    spisok_numbers.append(temp)                         # Как только цикл собирает целое число добавляем переменную в список
    temp = ''                                           # Сбрасываем переменныу
    j+=1

spisok_numbers = list(map(int,spisok_numbers))          # Переводим список чисел в int при помощи функции ускоренной обработки map
print(f'spisok_numbers:{spisok_numbers}')

spisok = []                                             # Сбрасываем начальный список элементов чтобы освободить переменную
i = 0
for e in spisok_numbers:
    spisok.append(e)
    spisok.append(spisok_operation[i])
    i+=1
spisok.pop()                                            # Удаляю последний элемент
print(spisok)


i = 0
j = 0
result = []
temp = float(0.0)
for e in spisok:
    if e == '*':
        e = spisok[i-1] * spisok[i+1]
        result.append(temp)
        spisok.pop(i+1)
        spisok.pop(i-1)
        i-=1
        e = result
    i+=1
i=0
for e in spisok:
    if e == '/':
        e = spisok[i-1] / spisok[i+1]
        result.append(temp)
        spisok.pop(i+1)
        spisok.pop(i-1)
        i-=1
        e = result
    i+=1
i=0
for e in spisok:
    if e == '+':
        temp = spisok[i-1] + spisok[i+1]
        result.append(temp)
        spisok.pop(i+1)
        spisok.pop(i-1)
        i-=1
        e = result
    i+=1
i=0
for e in spisok:
    if e == '-':
        e = spisok[i-1] - spisok[i+1]
        result.append(temp)
        spisok.pop(i+1)
        spisok.pop(i-1)
        i-=1
        e = result
    i+=1
i=0
print(result)