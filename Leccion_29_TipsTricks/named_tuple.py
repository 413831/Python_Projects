# Namedtuples son una extension
# Son una alternativa para escribir clases (atributos tipos inmutables)
# Asignar un identificador a cada elemento de la tupla
from collections import namedtuple
# Definimos una clase con atributos inmutables pero usando namedtuple
Persona1 = namedtuple('Persona1', 'nombre apellido edad')
# Creamos una instancia de la clase (se agrega un constructor por default con los atributos)
persona1 = Persona1('Juan','Perez',28)
print(persona1)

# Creamos nuestra clase con los atributos usando una lista
Persona2 = namedtuple('Persona2', ['nombre','apellido','edad'])
persona2 = Persona2('Pepito','Gomez',26)
print(persona2)

# Podemos acceder a los atri utos de manera individual por nombre
print(f'Nombre: {persona2.nombre}')
print(f'Apellido: {persona2.apellido}')
print(f'Edad: {persona2.edad}')
# Acceder a los atributos por índice
print(f'Nombre: {persona2[0]}')
print(f'Apellido: {persona2[1]}')
print(f'Edad: {persona2[2]}')
# Podemos convertir los valores a una tupla
print(tuple(persona2))
# Podemos hacer unpacking de los elementos de la tupla
nombre, apellido, edad = persona2
print(f'Valores tupla persona: {nombre}, {apellido}, {edad}')
# Podemos hacer unpacking pasando como argumento
print(*persona2)
# Las tuplas son inmutables al igual que namedtuple
# persona2.edad = 30

# Subclases de namedtuples
class Persona3(Persona2):
    # Agregamos un nuevo método a la clase hija
    def convertir_mayusculas(self):
        return f'Nombre completo: {self.nombre.upper()} {self.apellido.upper()}'

persona3 = Persona3('Marta','Salgado',34)
print(persona3)
print(persona3.convertir_mayusculas())

# Existe otra forma de hacer extends de la clase (la forma recomendada con namedtuple)
# nota: se utiliza el atributo especial fields
Persona4 = namedtuple('Persona4', Persona2._fields + ('email',))
# Creamos un objeto Persona4 con el nuevo atributo
persona4 = Persona4('Jose','Fernandez',55,'pepefer@mail.com')
print(persona4)

# Métodos de ayuda (built-in) en namedtuple
print(persona4._fields)
# Ej. convertir a un diccionario
# nota: se utiliza método especial asdict()
diccionario_persona4 = persona4._asdict()
print(diccionario_persona4)





