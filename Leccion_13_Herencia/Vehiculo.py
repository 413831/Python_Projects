class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehiculo[Color: {self.color}, Ruedas: {self.ruedas}]'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'Coche: [Velocidad: {self.velocidad} km/h] {super().__str__()}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Bicicleta: [Tipo: {self.tipo}] {super().__str__()}'


# TEST
vehiculo1 = Vehiculo('negro',5)
print(vehiculo1)

coche1 = Coche('blanco', 4, 200)
print(coche1)

bicicleta1 = Bicicleta('verde',2,'Deportiva')
print(bicicleta1)
