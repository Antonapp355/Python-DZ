import json
import view
import model_search

def Dell_Man():
    n = model_search.Search()
    print('\n============================================================================== \n')
    with open("name_book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    del data[n]
    with open('name_book.json', 'w', encoding='utf-8') as book:
        book.write(json.dumps(data , ensure_ascii=False))
    print('\n============================================================================== \n')
    print('Удалено.')
    input('Нажмине клавишу "Enter" для продолжения.')
    
