from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return f'Área rectángulo: {self.ancho * self.alto}'

    def __str__(self):
        return f'Clase Rectangulo: hereda:{FiguraGeometrica.__str__(self)} hereda: {Color.__str__(self)}'

if __name__ == '__main__':
    rectangulo1 = Rectangulo(3, 6, 'amarillo')
    print(rectangulo1.calcular_area())
