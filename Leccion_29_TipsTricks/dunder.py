# dunder = Double Underscore
# "magic methods"

class Padre:
    def __init__(self):
        # Al usar dunder al inicio y al final
        # No se aplica el concepto de name mangling
        self.__variable_privada = 10
        self.__variable_dunder__ = 15


if __name__ == '__main__':
    objeto = Padre()
    print(dir(objeto))
    print(f'Accediendo a la variable privada: {objeto._Padre__variable_privada}')
    print(f'Accediendo a la variable dunder: {objeto.__variable_dunder__}')
