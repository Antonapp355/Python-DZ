import model_id
import json
import view

# Добавление сотрудника в name_book
def Add_Name():
    data_personal = {
        'ID': model_id.iD_name(), 
        'Ф.И.О.': view.get_new_name(), 
        'тел.': view.get_new_telephone(),
        'Должность': view.get_post(),
        'Отдел' : view.get_office()
    }
    with open("name_book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    
    data.append(data_personal)
    with open('name_book.json', 'w', encoding='utf-8') as book:
        book.write(json.dumps(data , ensure_ascii=False))

# Добавление должности в post_book
def Add_new_Post():
    data_personal = {
        'ID': model_id.iD_Post(),
        'Должность': view.get_new_post()
    }
    with open("post_book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    
    data.append(data_personal)
    with open('post_book.json', 'w', encoding='utf-8') as book:
        book.write(json.dumps(data , ensure_ascii=False))


# Добавление отдела
def Add_new_Office():
    data_personal = {
        'ID': model_id.iD_Office(),
        'Отдел': view.get_new_office()
    }
    with open("office_book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    
    data.append(data_personal)
    with open('office_book.json', 'w', encoding='utf-8') as book:
        book.write(json.dumps(data , ensure_ascii=False))