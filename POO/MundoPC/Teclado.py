from Dispositivo_Entrada import Dispositivo_Entrada


class Teclado(Dispositivo_Entrada):
    contador_teclado = 0

    def __init__(self, tipo_entrada, marca):
        Teclado.contador_teclado += 1
        super().__init__(tipo_entrada, marca)
        self.id_teclado = Teclado.contador_teclado

    def __str__(self):
        return f'{super().__str__()} Teclado: [id_teclado: {self.id_teclado}]'


if __name__ == '__main__':
    teclado1 = Teclado('Teclado', 'dell')
    teclado2 = Teclado('Teclado', 'HP')
    teclado3 = Teclado('Teclado', 'Compac')
    teclado4 = Teclado('Teclado', 'LG')
    teclado5 = Teclado('Teclado', 'Samsung')

    teclado1.marca = 'Dells'

    print(teclado1)
    print(teclado2)
    print(teclado3)
    print(teclado4)
    print(teclado5)
