from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Diego', '4000000')
gerente = Gerente('Diego', 60000000, 'Sistemas')

imprimir_detalles(empleado)
imprimir_detalles(gerente)