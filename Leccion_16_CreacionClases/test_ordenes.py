from Producto import Producto
from Orden import Orden

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Medias', 30.00)
producto4 = Producto('Saco', 400.00)

productos1 = list([producto1, producto2])
productos2 = list([producto3, producto4])

orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)

orden2 = Orden(productos2)
print(orden1)
print(f'Total orden {orden1.id_orden}: ${orden1.calcular_total()}')
print(orden2)
print(f'Total orden {orden2.id_orden}: ${orden2.calcular_total()}')