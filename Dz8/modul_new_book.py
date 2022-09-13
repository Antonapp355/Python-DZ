import json
import view

def New_Book():
    new = view.create_new_book()
    p = []
    with open(f'{new}.json', 'w', encoding='utf-8') as book:
        book.write(json.dumps(p , ensure_ascii=False))
    input('Нажмине клавишу "Enter" для продолжения.')