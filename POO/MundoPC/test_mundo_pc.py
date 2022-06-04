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

raton1 = Raton('Ratón', 'Dell')
raton2 = Raton('Ratón', 'HP')
raton3 = Raton('Ratón', 'Compac')
raton4 = Raton('Ratón', 'LG')
raton5 = Raton('Ratón', 'Samsung')

teclado1 = Teclado('Teclado', 'dell')
teclado2 = Teclado('Teclado', 'HP')
teclado3 = Teclado('Teclado', 'Compac')
teclado4 = Teclado('Teclado', 'LG')
teclado5 = Teclado('Teclado', 'Samsung')

computadora1 = Computadora(monitor1, teclado1, raton1)
computadora2 = Computadora(monitor2, teclado2, raton2)
computadora3 = Computadora(monitor3, teclado3, raton3)
computadora4 = Computadora(monitor4, teclado4, raton4)
computadora5 = Computadora(monitor5, teclado5, raton5)

orden1 = Orden([computadora1, computadora2, computadora3, computadora4, computadora5])
print(orden1)