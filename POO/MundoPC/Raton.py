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
    raton1 = Raton('Ratón', 'Dell')
    raton2 = Raton('Ratón', 'HP')
    raton3 = Raton('Ratón', 'Compac')
    raton4 = Raton('Ratón', 'LG')
    raton5 = Raton('Ratón', 'Samsung')

    print(raton1)
    print(raton2)
    print(raton3)
    print(raton4)
    print(raton5)
