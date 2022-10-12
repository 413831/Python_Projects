# Diferencia entre variables de clase y de instancia (objeto)
class Perro:
    numero_patas = 4 # <- Variable de clase

    def __init__(self, nombre):
        self.nombre = nombre # <- Variable de instancia (objeto)

# Definimos objetos
layla = Perro('Layla')
venus = Perro('Venus')
# Cada objeto tiene su propio atributo de nombre
print(layla.nombre, venus.nombre)

# La variable se clase s epuede acceder con el nombre de la clase o con objetos
print(layla.numero_patas, venus.numero_patas, Perro.numero_patas)

# Si tratamos de acceder la variable de instancia desde la clase no es posible
# print(Perro.nombre)

# Si queremos modificar el numero_patas para todos los perros
Perro.numero_patas = 5
print(layla.numero_patas, venus.numero_patas, Perro.numero_patas)

# Si queremos modificar el numero_patas para un solo perro
venus.numero_patas = 6 # Se crea una variable de instancia (oculta a la variable de clase)
print(layla.numero_patas, venus.numero_patas, Perro.numero_patas)

# Imprimimos el valor de la variable de instancia y la variable de clase
print(venus.numero_patas, venus.__class__.numero_patas)

# Se crea una variable de la clase en tiempo de ejecución
Perro.nombre = 'Clase Perro'
print(layla.nombre, venus.nombre, Perro.nombre)

# Si definimos una variable de clase que no está en los objetos
Perro.numero_orejas = 2
print(layla.numero_orejas, venus.numero_orejas, Perro.numero_orejas)
############################
# Contador de objetos de una clase
# Implementacion Erronea
class ContadorObjetosErronea:
    numero_instancias = 0

    def __init__(self):
        # Aca está el error
        self.numero_instancias += 1

print('Contador de Instancias Erroneo:')
print(ContadorObjetosErronea.numero_instancias)
print(ContadorObjetosErronea().numero_instancias)
print(ContadorObjetosErronea().numero_instancias)
print(ContadorObjetosErronea.numero_instancias)

# Implementación corregida
class ContadorObjetos:
    numero_instancias = 0

    def __init__(self):
        # Incrementamos la variable de clase
        self.__class__.numero_instancias += 1

print('Contador de Instancias:')
print(ContadorObjetos.numero_instancias)
print(ContadorObjetos().numero_instancias)
print(ContadorObjetos().numero_instancias)
print(ContadorObjetos().numero_instancias)

