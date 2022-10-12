class Persona:
    # constructor
    # método double underscore o dunder
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} años')

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self.apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,edad):
        self.edad = edad

    def __del__(self):
        print(f'Persona {self.nombre} {self.apellido}')


# la variable global __name__ indica el módulo que se ejecuta
if __name__ == '__main__':
    # nota: se pueden crear atributos de clase de forma dinamica
    Persona.telefono = 143243242

    persona1 = Persona('Pepito', 'Gonzalez', 28)
    # persona1.mostrar_detalle()
    Persona.mostrar_detalle(persona1)
    print(persona1.telefono)

    persona2 = Persona('Carmen', 'Sandiego', 45)
    # persona2.mostrar_detalle()
    Persona.mostrar_detalle(persona2)
    print(persona2.telefono)

    # nota: con el decorador property se accede a los atributos indirectamente
    print(persona2.nombre)


print(__name__)