class Monitor:
    contador_monitor = 0

    def __init__(self, marca, tamano):
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self._marca = marca
        self._tamano = tamano

    @property
    def id_monitor(self):
        return self._id_monitor

    @id_monitor.setter
    def id_monitor(self, id_monitor):
        self._id_monitor = id_monitor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano

    def __str__(self):
        return f'Monitor: [Id Monitor: {self.id_monitor}] [Marca: {self.marca}] [Tamaño: {self.tamano}]'

if __name__ == '__main__':
    monitor1 = Monitor('Dell', '22´')
    monitor2 = Monitor('HP', '22´')
    monitor3 = Monitor('Compac', '22´')
    monitor4 = Monitor('LG', '22´')
    monitor5 = Monitor('Samsung', '22´')

    monitor2.tamano = '14'
    monitor3.tamano = '16'
    monitor4.tamano = '18'
    monitor5.tamano = '27'

    print(monitor1)
    print(monitor2)
    print(monitor3)
    print(monitor4)
    print(monitor5)