class Cubo:

    def __init__(self, ancho, profundidad, altura):
        self.ancho = ancho
        self.profundidad = profundidad
        self.altura = altura

    def calcular_volumen(self):
        return self.ancho * self.profundidad * self.altura

#TEST
ancho = int(input("Proporciona el ancho: "))
profundidad = int(input("Proporciona la profundidad: "))
altura = int(input("Proporciona la altura: "))
cubo = Cubo(ancho, profundidad, altura)

print(f'Volúmen cubo: {cubo.calcular_volumen()}')

