# Decoradores de Clase
# Permiten transformar de manera programática nuestra clase
# Es similar a los decoradores de funciones (es metaprogramación)
import inspect


def decorador_repr(cls):
    print('1. Se ejecuta decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')
    # Revisamos los atributos de la clase con el método vars
    atributos = vars(cls)
    # Iteramos cada atributo
    for nombre, atributo in atributos.items():
        print(nombre, atributo)

    # Revisamos sise ha sobreescrito el método __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método __init__')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma método __init__: {firma_init}')
    # Recuperamos los parámetros, excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parámetros init: {parametros_init}')

    # Revisamos si por cada parámetro tiene un método property asociado
    for parametro in parametros_init:
        # property es un valor de tipo built-in, es una clase
        # Se utiliza para verificar si se usa el decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un método property para el parámetro {parametro}')
    # Crear el método repr dinamicamente
    def metodo_repr(self):
        # Obtenemos el nombre de la clase dinámicamente
        nombre_clase = self.__class__.__name__
        print(f'Nombre clase: {nombre_clase}')

        # Obtenemos los nombre de las propiedades y sus valores dinámicamente
        # Expresión generadora, crear nombre_atr = valor_atr
        generador_arg = (f'{nombre}={getattr(self,nombre)!r}' for nombre in parametros_init)
        lista_arg = list(generador_arg)
        print(f'Lista del generador: {lista_arg}')
        # Creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del método repr: {argumentos}')
        # Creamos la forma del método __repr__, sin su nombre
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'
        print(f'Resultado método repr: {resultado_metodo_repr}')
        return resultado_metodo_repr

    # Agregar dinámicamente el método repr a nuestra clase
    setattr(cls,'__repr__',metodo_repr)

    return cls


@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print('2. Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

#    def __repr__(self):
#        return f'Persona({self._nombre}, {self._apellido})'

persona1 = Persona('Pepito','Gonzalez', 27)
print(persona1)
persona2 = Persona('Karla','Gomez', 33)
print(persona2)
# dir - Obtener los métodos de propiedad nombre, apellido, repr asociados a la clase
print(dir(Persona))
# getsource - Obtener código del método repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)