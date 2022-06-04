from FiguraGeometrica import FiguraGeometrica
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creación objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(-3, 'rojo')
print(cuadrado1)
cuadrado1.ancho = 9
cuadrado1.alto = 9

print(cuadrado1.calcular_area())
print(cuadrado1)



print('Creación objeto rectángulo'.center(50, '-'))
rectangulo1 = Rectangulo(9, 8, 'azul')
print(rectangulo1)

# figura1 = FiguraGeometrica()
