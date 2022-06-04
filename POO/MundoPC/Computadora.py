class Computadora:
    contador_computadora = 0

    def __init__(self, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self._id_computadora = Computadora.contador_computadora
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def id_computadora(self):
        return self._id_computadora

    @id_computadora.setter
    def id_computadora(self, id_computadora):
        self._id_computadora = id_computadora

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'-> Computadora: [Id Computadora: {self.id_computadora}] \n [Monitor: {self.monitor}] \n [Teclado: {self.teclado}] \n [Ratón: {self.raton}] \n'

if __name__ == '__main__':
    computador1 = Computadora('Monitor1', 'Teclado1', 'Raton1')
    computador2 = Computadora('Monitor1', 'Teclado2', 'Raton2')
    computador3 = Computadora('Monitor3', 'Teclado1', 'Raton3')
    computador4 = Computadora('Monitor4', 'Teclado4', 'Raton1')
    computador5 = Computadora('Monitor5', 'Teclado5', 'Raton5')

    computador2.monitor = 'Monitor2'
    computador3.teclado = 'Teclado3'
    computador4.raton = 'Raton4'

    print(computador1)
    print(computador2)
    print(computador3)
    print(computador4)
    print(computador5)