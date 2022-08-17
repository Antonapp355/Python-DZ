import view
import menu_model
import model_log

def button_click():
    value_m = view.menu()
    model_log.get_log(menu_model.menu_operation(value_m))
    if value_m == 5:
        return exit
    if value_m != 5:
        button_click()
