from asyncore import read
from this import d
import view
import json

def Search():
    with open("office_book.json", "r", encoding = 'utf-8') as read_file:
        data_office = list(json.load(read_file))
    with open("post_book.json", "r", encoding = 'utf-8') as read_file:
        data_post = list(json.load(read_file))
    with open("name_book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    number_search = view.search_string()
    if number_search == 1:
        number_ID = int(input("Введите ID сотрудника: "))
        i = 0
        for e in data:
            if number_ID == e['ID']:
                print(f'\n============================================================================== \n{e}')
                i += 1
                temp_post = data[i]['Должность']
                temp_office = data[i]['Отдел']
                print(f'{data_post[temp_post-1]} \n{data_office[temp_office-1]} \n============================================================================== \n')
                return i
            else:
                continue
            i += 1
    if number_search == 2:
        i = 0
        name = str(input('Введите имя сотрудника: '))
        for e in data:
            if name == e['Ф.И.О.']:
                print(f'\n============================================================================== \n{e}')
                i += 1
                temp_post = data[i]['Должность']
                temp_office = data[i]['Отдел']
                print(f'{data_post[temp_post-1]} \n{data_office[temp_office-1]} \n============================================================================== \n')
                return i
            else:
                continue
            i += 1
    if number_search == 3:
        i = 0
        tel = str(input('Введите телефон сотрудника: '))
        for e in data:
            if tel == e['тел.']:
                print(f'\n============================================================================== \n{e}')
                i += 1
                temp_post = data[i]['Должность']
                temp_office = data[i]['Отдел']
                print(f'{data_post[temp_post-1]} \n{data_office[temp_office-1]} \n============================================================================== \n')
                return i
            else:
                continue
            i += 1
    if number_search == 4:
        i = 0
        post_search = view.get_post()
        for e in data:
            if post_search == e['Должность']:
                print(f'\n============================================================================== \n{e}')
                i += 1
                temp_post = data[i]['Должность']
                temp_office = data[i]['Отдел']
                print(f'{data_post[temp_post-1]} \n{data_office[temp_office-1]} \n============================================================================== \n')
                return i
            else:
                continue
            i += 1
    if number_search == 5:
        i = 0
        post_search = view.get_office()
        for e in data:
            if post_search == e['Отдел']:
                print(f'\n============================================================================== \n{e}')
                i += 1
                temp_post = data[i]['Должность']
                temp_office = data[i]['Отдел']
                print(f'{data_post[temp_post-1]} \n{data_office[temp_office-1]} \n============================================================================== \n')
                return i
            else:
                continue
            i += 1
    input('Нажмине клавишу "Enter" для продолжения.')