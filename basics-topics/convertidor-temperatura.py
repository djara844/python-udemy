grados_celsius = float(input('Ingrese temperatura en grados Celsius: '))
grados_fahrenheit = float(input('Ingrese temperatura en grados Fahrenheit: '))


def celsius_to_fahrenheint(celsius):
    return celsius * 1.8 + 32


def fahrenheint_to_celsius(fahrenheint):
    return (fahrenheint - 32) * 5 / 9


print(f'Celsius a Fahrenheint: {celsius_to_fahrenheint(grados_celsius)}')

print(f'Fahrenheint a Celsius: {fahrenheint_to_celsius(grados_fahrenheit)}')

"""
"""

# dsds
