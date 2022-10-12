# from mi_modulo import *
from mi_modulo import funcion_publica
from mi_modulo import _funcion_protegida

class MiClase:
    def __init__(self):
        self.mi_variable_publica = 10
        self._mi_variable_protegida =10

# El guión bajo al final se usa para evitar conflictos con nombres (keywords)
def funcion1(nombre, class_):
    print('funcion que recibe una clase')


if __name__ == '__main__':
    objeto = MiClase()
    print(objeto.mi_variable_publica)
    # No se deben acceder a metodos o atributos con guion bajo al inicio
    print(objeto._mi_variable_protegida)

    # Accedemos a las funciones del módulo importado
    funcion_publica()
    # No se pueden utilizar funciones protegidas fuera de su módulo o clase
    _funcion_protegida()

    # Ejemplos con guion bajo final
    funcion1('mensaje',MiClase)
