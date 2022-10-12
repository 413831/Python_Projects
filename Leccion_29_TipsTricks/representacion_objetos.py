# __str__ su objetivo es que la informacion sea legible para el usuario
# __repr__ su objetivo es que la información no sea ambigua
# se utiliza para hacer debugging (formato tipo constructor)
# La implementación por default del método str llama a repr

class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

# Por default solo se muestra el nombre dela clase y el id del objeto (direccion de memoria)
audi_a3 = Auto('audi','A3','violeta')
print(audi_a3)

class AutoStr:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f'str: Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}'

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.marca!r}, {self.modelo!r}, {self.color!r})')

audi_a1 = AutoStr('audi','A1','blanco')
print(audi_a1)
print(audi_a1.__str__())
print(str(audi_a1))
print('{}'.format(audi_a1))
print(f'{audi_a1}')

# Sin embargo es mas recomendable usar __repr__ en lugar de __str__
# Ej. cualquier colección utiliza repr en lugar de str para mostrar la información
print([audi_a1])
# También usando !r
print(f'{audi_a1!r}')

# También manualmente podemos escoger qué método utilizar
print(str(audi_a1))
print(repr(audi_a1))