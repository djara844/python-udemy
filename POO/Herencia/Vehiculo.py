class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehiculo: {self.color} {self.ruedas}'


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'Coche: {self.velocidad} Hereda: {super().__str__()}'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Bicicleta: {self.tipo} Hereda: {super().__str__()}'


vehiculo1 = Vehiculo('azul', 3)
print(vehiculo1)

coche1 = Coche('rojo', 6, '70km-h')
print(coche1)

bicicleta1 = Bicicleta('verde', 2, "Todo terreno")
print(bicicleta1)
