# Con doble guion bajo, no solo es una convencion
# afecta la forma en que se acceden los atributos o metodos

class Padre:
    def __init__(self):
        self.variable_publica = 1
        self._variable_protegida = 2
        self.__variable_privada = 3

    def get_variable_privada(self):
        return self.__variable_privada

    def __metodo_privado(self):
        print('Accediendo metodo privado padre...')


class Hijo(Padre):
    def __init__(self):
        super().__init__()
        self.variable_publica = 'sobreescrita 1'
        self._variable_protegida = 'sobreescrita 2'
        self.__variable_privada = 'sobreescrita 3'

    def __metodo_privado(self):
        print('Accediendo método privado hijo')

# Prueba usando una variable global
_Prueba__variable_global = 10

class Prueba:
    def obtener_variable(self):
        return __variable_global



if __name__ == '__main__':
    # Imprimir todos los atributos de la clase
    padre = Padre()
    print(dir(padre))
    #Accedemos a los atributos de la clase
    print(f'Variable pública: {padre.variable_publica}')
    print(f'Variable protegida: {padre._variable_protegida}')
    # print(f'Variable privada: {padre.__variable_privada}')
    print(f'Variable privada usando name mangling: {padre._Padre__variable_privada}')

    # Name mangling es transparente para el programador
    print(f'Acceso por medio del método get: {padre.get_variable_privada()}')

    # Prueba de la clase Hijo
    hijo = Hijo()
    print(f'Atributo público desde hijo: {hijo.variable_publica}')
    print(f'Atributo protegido desde hijo: {hijo._variable_protegida}')
    # print(f'Atributo privado desde hijo: {hijo.___variable_privada}')
    # Utilizando name mangling desde la clase hijo
    print(f'Atributo privado desde hijo con name mangling: {hijo._Hijo__variable_privada}')
    print(f'Atributo privado desde hijo a la clase padre: {hijo._Padre__variable_privada}')

    # También podemos usar métodos con doble guión bajo
    # padre.__metodo_privado() ERROR
    padre._Padre__metodo_privado()
    # Ahora desde la clase hijo
    hijo._Hijo__metodo_privado()
    hijo._Padre__metodo_privado()

    # Accediendo a una variable global
    prueba = Prueba()
    print(f'Accediendo variable global: {_Prueba__variable_global}')
    print(f'Accediendo variable global desde una clase: {prueba.obtener_variable()}')
