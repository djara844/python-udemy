# ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroreno: {ancho}')

        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroreno: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroreno: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroreno: {alto}')

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'Figura geométrica Ancho: {self._ancho} Alto: {self._alto}'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False

if __name__ == '__main__':
    figura1 = FiguraGeometrica(4, 5)
    print(figura1)
