
from fractions import Fraction


def menu():
    print(' *************************************** \n * 1.Журнал                            * \n * 2.Примитивный калькулятор           * \n * 3.Операции над комплексными числами * \n * 4.Операции с рациональными числами  * \n * 5.Выход                             * \n *************************************** ')
    return int(input('Введите номер операции: '))


def get_value_1():
    return int(input('Value 1: '))
def get_value_2():
    return int(input('Value 2: '))
def get_operation():
    return str(input('Operation (+,-,*,/): '))

def get_complex_value_1():
    return complex(input('Value 1 (1+1j): '))
def get_complex_value_2():
    return complex(input('Value 2 (1+1j): '))

def get_rational_value_1():
    return Fraction(input('Value 1 (1/3): '))
def get_rational_value_2():
    return Fraction(input('Value 2 (1/3): '))

def view_result(data):
    print(data)