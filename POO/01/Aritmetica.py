class Aritmetica:
    """
    Clase Aritmética
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


test = Aritmetica(2, 4)
print(f'La suma es: {test.sumar()}')
print(f'La resta es: {test.restar()}')
print(f'La multiplicación es: {test.multiplicar()}')
print(f'La división es: {test.dividir()}')
