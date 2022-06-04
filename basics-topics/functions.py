def suma(*args):
    result = 0
    for arg in args:
        result += arg
    return result
print(suma(3, 5, 9, 19))

def multiplicar(*args):
    result = 1
    for arg in args:
        result *= arg
    return  result
print(multiplicar(9, 8, 20))

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
result = factorial(5)
print(f'El factorial de 5 es {result}')

def show_numbers(number):
    if number >= 1:
        print(number)
        show_numbers(number - 1)
show_numbers(6)