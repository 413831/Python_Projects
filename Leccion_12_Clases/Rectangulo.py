class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> int:
        return self.base * self.altura


# TEST
base = int(input("Proporciona la base: "))
altura = int(input("Proporciona la altura: "))
rectangulo = Rectangulo(base,altura)

print(f'Área rectángulo: {rectangulo.calcular_area()}')