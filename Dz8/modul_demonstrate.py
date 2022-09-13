import json


def Demonstrate():
    with open("name_book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
        print('\n============================================================================== \n')
        for e in data:
            print(e)
    with open("office_book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
        print('\n============================================================================== \n')
        for e in data:
            print(e)
    with open("post_book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
        print('\n============================================================================== \n')
        for e in data:
            print(e)
        print('\n============================================================================== \n')
    input('Нажмине клавишу "Enter" для продолжения.')