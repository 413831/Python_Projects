class Clase1:

    def __init__(self):
        print('Clase1.__init__')

    def metodo(self):
        print('Método clase 1')


class Clase2(Clase1):

    def __init__(self):
        print('Clase2.__init__')
        super().__init__()

    def metodo(self):
        print('Método clase 2')
        super().metodo()


class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
        super().__init__()

    def metodo(self):
        print('Método clase 3')
        super().metodo()

class Clase4(Clase2, Clase3):
    def metodo(self):
        print('Método clase 4')
        super().metodo()

# Creamos objeto clase4
clase4 = Clase4()

# __bases__
print(Clase4.__bases__)

# mro
print(Clase4.mro())

# cual método se ejecuta
clase4.metodo()