import modul_new_book
import model_exit
import modul_add
import model_search
import model_del
import modul_demonstrate

number_menu = 0

def menu_init(m):
    global number_menu
    number_menu = m

def menu_operation(m):
    if m == 1:
        print('1.Создать новую книгу сотрудников.')
        modul_new_book.New_Book()
    if m == 2:
        print('2.Добавить сотрудника.')
        modul_add.Add_Name()
    if m == 3:
        print('3.Добавить новые должности.')
        modul_add.Add_new_Post()
    if m == 4:
        print('4.Добавить новый отдел.')
        modul_add.Add_new_Office()
    if m == 5:
        print('5.Редактировать.')
        model_del.Dell_Man()
        print('\n============================================================================== \nВведите новые данные.')
        modul_add.Add_Name()
    if m == 6:
        print('6.Удалить.')
        model_del.Dell_Man()
    if m == 7:
        print('7.Поиск по книге.')
        model_search.Search()
    if m == 8:
        print('8.Ппоказать книгу.')
        modul_demonstrate.Demonstrate()
    if m == 9:
        print('9.Выход.')
        return model_exit.exit()
