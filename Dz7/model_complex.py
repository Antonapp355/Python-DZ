number_1 = 0 + 0j
number_2 = 0 + 0j
operation = ''

def calculator_init(a,b,o,):
    global number_1
    global number_2
    global operation
    number_1 = a
    number_2 = b
    operation = o


def sum(a,b):
    result = a+b
    print(f'Result = {result}')
    return result

def subtraction(a,b):
    result = a-b
    print(f'Result = {result}')
    return result

def multiplication (a,b):
    result = a*b
    print(f'Result = {result}')
    return result

def divide (a,b):
    result = a/b
    print(f'Result = {result}')
    return result

def calculator_operation(o):
    if o == '+':
        return sum(number_1,number_2)
    if o == '-':
        return subtraction(number_1,number_2)
    if o == '*':
        return multiplication(number_1,number_2)
    if o == '/':
        return divide(number_1,number_2)