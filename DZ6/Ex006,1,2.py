# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

import re
from fileinput import close
import json

fraza = str(input('Введите фразу: '))

def RLE(fraza):                                                         # Создаём сжатую фразу на основе вводных данных
    spisok = list(map(str,fraza))
    spisok_nums = []
    spisok_char = []
    i=1
    temp = ''
    for e in spisok:
        if e == temp:
            i+=1
        if e != temp:
            spisok_nums.append(i)
            i=1
        if i == 1:
            spisok_char.append(e)
        temp = e
    spisok_nums.append(i)
    spisok_nums.reverse()
    spisok_nums.pop()
    spisok_nums.reverse()
    result = ''
    i = 0
    for e in spisok_nums:
        if e == 1:
            result += str(spisok_char[i])
        if e > 1:
            result += str(spisok_nums[i])
            result += str(spisok_char[i])
        i+=1
    return result

print(RLE(fraza))

def Upload_Files(fraza):                                                # Записываем фразу в файл
    with open('new_RLE_fraza.json', 'w', encoding = 'utf-8') as fh:
        fh.write(json.dumps(fraza, ensure_ascii= False))
    print('Файл 1 записан: new_RLE_fraza.json')
Upload_Files(RLE(fraza))

def File_Read(spisok1):                                                 # Считываем фразу с файла
    with open('new_RLE_fraza.json', 'r', encoding = 'utf-8') as fh:
        spisok1 = list(json.load(fh))
    
    return spisok1
File_Read(RLE(fraza))

rle_fraza = RLE(fraza)

def RLE_Reverse(rle_fraza):                                             # Восстанавливаем фразу
    spisok_rle_fraza = list(map(str,rle_fraza))
    spisok_result = []
    i = 0
    while i < len(spisok_rle_fraza):
        if spisok_rle_fraza[i].isdigit():
            spisok_result.append(spisok_rle_fraza[i])
        else:
            spisok_result.append(spisok_rle_fraza[i])
            spisok_result.append('.')
        i+=1
    spisok_result.append('7')
    spisok_result_fraza = []
    i = 0
    for e in spisok_result:
        spisok_result_fraza.append(e)
        if e == '.':
            if spisok_result[i+1].isdigit():
                spisok_result_fraza.append(e)
            else:
                spisok_result_fraza.append('1')
                spisok_result_fraza.append(spisok_result[i])
        i+=1
    spisok_result_fraza.pop()
    rle_reverseve_fraza = ''
    for e in spisok_result_fraza:
        if e == '.':
            continue
        else:
            rle_reverseve_fraza += e
    spisok_numbers_str = re.findall(r'(\d{1,})', rle_reverseve_fraza)
    spisok_numbers = list(map(int,spisok_numbers_str))

    spisok_char = []
    for e in spisok_result_fraza:
        if e.isdigit() or e == '.':
            continue
        else:
            spisok_char.append(e)

    not_rle_fraza = ''
    i=0
    j=0
    for e in spisok_char:
        while i < spisok_numbers[j]:
            not_rle_fraza += e
            i+=1
        j+=1
        i=0
    return not_rle_fraza

print(RLE_Reverse(rle_fraza))

def Upload_Files(fraza):                                                # Загружаем востановленную фразу в новый файл
    with open('not_RLE_fraza.json', 'w', encoding = 'utf-8') as fh:
        fh.write(json.dumps(fraza, ensure_ascii= False))
    print('Файл 1 записан: not_RLE_fraza.json')

Upload_Files(RLE_Reverse(rle_fraza))