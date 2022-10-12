# ABC - Abstract Base Class
# Nos permite asegurar que las clases que heredan implementen los métodos
# ABC permite escribir una jerarquia de clases más robusta y escribir código más mantenible
# Ej. Sin usar ABC y los posible problemas
from abc import ABCMeta, abstractmethod


class ClaseBase1:
    def metodo_1(self):
        raise NotImplementedError

    def metodo_2(self):
        raise NotImplementedError

class ClaseConcreta1(ClaseBase1):

    # Implementación de la clase padre
    def metodo_1(self):
        print('Metodo 1 implementado...')

    # El método 2 no se va a implementar
    # Esta es un problema por que no se repotar la falta de implementación


# Hay un problema porque se puede instanciar la clase base
# clase_base = ClaseBase1()
# clase_base.metodo_1()

# Esto funciona según lo esperado
clase_concreta = ClaseConcreta1()
# clase_concreta.metodo_1()
# El método2, se llama el método heredado
# clase_concreta.metodo_2()

# Vamos a resolver los detalles anteriores usando ABC (Abstract Base Class)
class ClaseBase2(metaclass=ABCMeta):
    # No tenemos que agregar la implementación al ser un método abstracto
    @abstractmethod
    def metodo_1(self):
        pass

    @abstractmethod
    def metodo_2(self):
        pass


class ClaseConcreta2(ClaseBase2):
    def metodo_1(self):
        print('Método 1 implementado...')

    # Dejamos sin implementar el metodo_2
    # Estamos obligados a implementar todos los métodos abstractos
    def metodo_2(self):
        print('Método 2 implementado')



# Intentamos crear un objeto de la clase base
# clase_base = ClaseBase2()
# Instanciamos la clase concreta 2
clase_concreta = ClaseConcreta2()
clase_concreta.metodo_1()
clase_concreta.metodo_2()

