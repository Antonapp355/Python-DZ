import calculator_model
import view
import model_exit
import model_log
import model_complex
import model_fraction

number_menu = 0

def menu_init(m):
    global number_menu
    number_menu = m

def menu_operation(m):
    if m == 1:
        print('1.Журнал.')
        model_log.show_log()
        return '1.Журнал.'
    if m == 2:
        print('2.Примитивный алькулятор.')
        value_a = view.get_value_1()
        value_b = view.get_value_2()
        value_o = view.get_operation()
        calculator_model.calculator_init(value_a,value_b,value_o) 
        result = calculator_model.calculator_operation(value_o)
        view.view_result(result)
        return '2.Примитивный алькулятор.', value_a, value_o, value_b, '=', result
    if m == 3:
        print('3.Операции с комплексными числами.')
        value_a = view.get_complex_value_1()
        value_b = view.get_complex_value_2()
        value_o = view.get_operation()
        model_complex.calculator_init(value_a,value_b,value_o) 
        result = model_complex.calculator_operation(value_o)
        view.view_result(result)
        return '3.Операции с комплексными числами.', value_a, value_o, value_b, '=', result
    if m == 4:
        print('4.Операции с рациональными числами.')
        value_a = view.get_rational_value_1()
        value_b = view.get_rational_value_2()
        value_o = view.get_operation()
        model_fraction.calculator_init(value_a,value_b,value_o) 
        result = model_fraction.calculator_operation(value_o)
        view.view_result(result)
        return '4.Операции с рациональными числами.', value_a, value_o, value_b, '=', result
    if m == 5:
        print('5.Выход.')
        return model_exit.exit()
