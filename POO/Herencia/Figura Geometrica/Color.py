class Color:
    def __init__(self, color):
        self._color = color

    def __str__(self):
        return f'Color: {self._color}'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

if __name__ == '__main__':
    color1 = Color('azul')
    color1.color = 'rojo'
    print(color1.color)