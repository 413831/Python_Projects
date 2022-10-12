from Persona import Persona

print("Creacion de objetos".center(30,'-'))
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()

print("Eliminación de objetos".center(30,'-'))
# nota: no es comun utilizar el destructor porque existe el recolector de basura
del persona1
# print(__name__)