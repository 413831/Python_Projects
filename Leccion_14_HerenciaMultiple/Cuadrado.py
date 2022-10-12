from FiguraGeometrica import FiguraGeometrica
from Color import Color

# nota: el orden de definición de la herencia define el MRO
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self,lado, lado)
        Color.__init__(self,color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
