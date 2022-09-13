import view
import menu_model

def button_click():
    value_m = view.menu()
    menu_model.menu_operation(value_m)
    if value_m == 9:
        return exit
    if value_m != 9:
        button_click()
