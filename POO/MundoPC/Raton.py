from Dispositivo_Entrada import Dispositivo_Entrada


class Raton(Dispositivo_Entrada):
    contador_raton = 0

    def __init__(self, tipo_entrada, marca):
        Raton.contador_raton += 1
        super().__init__(tipo_entrada, marca)
        self._id_raton = Raton.contador_raton

    def __str__(self):
        return f'{super().__str__()} Ratón: [id_raton: {self._id_raton}]'


if __name__ == '__main__':
    raton1 = Raton('USB', 'Dell')
    raton2 = Raton('USB', 'HP')
    raton3 = Raton('USB', 'Compac')
    raton4 = Raton('USB', 'LG')
    raton5 = Raton('USB', 'Samsung')

    print(raton1)
    print(raton2)
    print(raton3)
    print(raton4)
    print(raton5)
