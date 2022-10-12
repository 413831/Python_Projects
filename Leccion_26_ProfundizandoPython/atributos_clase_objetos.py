class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Mostrar los atributos de un objeto
persona1 = Persona('Pepito','Gonzalez')
print(persona1.__dict__)

# Crear un atributo al vuelo
print(persona1.contador_personas) # Accediendo al atributo de clase
# No es posible modificarlo con el objeto, sino con la clase
persona1.contador_personas = 10
print(persona1.__dict__)
# El atributo anterior oculta al atributo de clase
print(Persona.contador_personas) # Atributo clase
print(persona1.contador_personas) # Atributo de objeto

# Creacion de segundo objeto
persona2 = Persona('Manolo','Navarro')
print(persona2.__dict__)

# Asociar un atributo de clase al vuelo
# ERROR
# print(Persona.contador2)

Persona.contador2 = 20




