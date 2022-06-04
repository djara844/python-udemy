from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return f'Área cuadrado: {self.ancho * self.alto}'

    def __str__(self):
        return f'Clase cuadrado: hereda {FiguraGeometrica.__str__(self)} hereda {Color.__str__(self)}'

if __name__ == '__main__':
    cuadrado1 = Cuadrado(3, 5, 'azul')
    print(cuadrado1.calcular_area())

