from Orden import Orden
from Producto import Producto

producto1 = Producto('Camisa', 100)
producto2 = Producto('Camisa', 200)
producto3 = Producto('Calcetines', 50)
producto4 = Producto('Bluza', 150)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(f'{orden1}'
      f'\nTotal Orden 1: {orden1.calcular_total()}')
orden2 = Orden(productos2)
print(f'{orden2}'
      f'\nTotal Orden 1: {orden2.calcular_total()}')
