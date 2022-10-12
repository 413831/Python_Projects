class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'


persona1 = Persona('Pepito', 32)
print(persona1)

persona2 = Persona('Marta', 53)
print(persona2)

persona3 = Persona('Kevin', 24)
print(persona3)
print(Persona.contador_personas)
