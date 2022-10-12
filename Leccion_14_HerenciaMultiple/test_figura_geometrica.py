from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creación Objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')

# MRO - Method Resolution Order
# nota: Se define en base al orden de cómo se heredan las clases
# print(Cuadrado.mro())
print(cuadrado1)

print('Creación Objeto rectángulo'.center(50,'-'))
rectangulo1 = Rectangulo(ancho=3, alto=8, color='verde')
print(f'Cálculo área rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)