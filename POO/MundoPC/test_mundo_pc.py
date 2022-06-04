from Monitor import Monitor
from Raton import Raton
from Teclado import  Teclado
from Computadora import Computadora
from Orden import Orden

monitor1 = Monitor('Dell', '22´')
monitor2 = Monitor('HP', '22´')
monitor3 = Monitor('Compac', '22´')
monitor4 = Monitor('LG', '22´')
monitor5 = Monitor('Samsung', '22´')

raton1 = Raton('USB', 'Dell')
raton2 = Raton('USB', 'HP')
raton3 = Raton('USB', 'Compac')
raton4 = Raton('USB', 'LG')
raton5 = Raton('USB', 'Samsung')

teclado1 = Teclado('USB', 'dell')
teclado2 = Teclado('USB', 'HP')
teclado3 = Teclado('USB', 'Compac')
teclado4 = Teclado('USB', 'LG')
teclado5 = Teclado('USB', 'Samsung')

computadora1 = Computadora(monitor1, teclado1, raton1)
computadora2 = Computadora(monitor2, teclado2, raton2)
computadora3 = Computadora(monitor3, teclado3, raton3)
computadora4 = Computadora(monitor4, teclado4, raton4)
computadora5 = Computadora(monitor5, teclado5, raton5)

orden1 = Orden([computadora1, computadora2, computadora3, computadora4, computadora5])
orden1.agregar_computadora(computadora5)
print(orden1)