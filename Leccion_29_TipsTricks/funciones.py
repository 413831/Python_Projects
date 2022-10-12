# Las funciones en python ciudadanos de primera clase
def mayusculas(texto):
    return texto.upper()

# Uso normal de una función
print(mayusculas('Hola'))

# Uso de una función como un objeto
# Asignar la referencia de la función a una variable, sin los paréntesis
variable_funcion = mayusculas
print(f'Función mayusculas: {mayusculas}')
print(f'Variable función: {variable_funcion}')

# Utilizamos la variable función en cualquier momento
print(variable_funcion('Texto'))

# Para demostrar que las funciones son objetos, eliminamos la referencia original
# del mayusculas

# Aun así, se puede utilizar función con la variable_función
print(variable_funcion('Otro texto'))

# Podemos saber el nombre por default que se le asigna a una función
print(f'Nombre por default de la función: {variable_funcion.__name__}')
# print(mayusculas('Nombre por default'))

# Cómo almacenar una función en una estructura de datos (list)
lista_funciones = [mayusculas, variable_funcion, str.upper]
print(lista_funciones)

for funcion in lista_funciones:
    print(funcion, funcion('Saludos desde la función'))

# 0 podemos acceder directamente a la función que deseemos
print(lista_funciones[1]('Saludos desde variable función'))

######################
# Podemos pasar funciones a otras funciones
# ** higher-order functions **
def saludar(argumento_funcion):
    # Se utiliza la funcion que se recibe como argumento y se devuelve la referencia
    referencia_funcion_retornada = argumento_funcion('Hola, saludos desde mi función')
    print(referencia_funcion_retornada)

# Llamamos la función saludar
saludar(mayusculas)

# Pasar una nueva implementación de la función que pasamos como argumento
def minusculas(texto):
    return texto.lower()

saludar(minusculas)

# Funcion map()
# toma una función como referencia, y un iterable
print(list(map(mayusculas, ['texto1', 'texto2', 'texto3'])))
print(list(map(minusculas, ['texto1', 'texto2', 'texto3'])))
#######################
# Funciones Anidadas
def mostrar(texto):
    # Definición de la función interna o anidada
    def convertir_minusculas(t):
        return t.lower()
    # Una vez definida la función interna, la llamamos
    return convertir_minusculas(texto)

# Cada vez que se llama la función mostrar
# se crea la función interna convertir_minusculas
print(mostrar('Texto desde función anidada'))

# No podemos utilizar la función interna desde fuera de la función externa
# convertir_minusculas('texto1')
# mostrar.convertir_minusculas('texto1')

# Retornar la función anidada
# Observar que en ningún momento se llama la función anidada desde la función externa
def hablar(volumen):
    def minusculas(texto):
        return texto.lower()
    def mayusculas(texto):
        return texto.upper()
    if volumen > 0.5:
        return mayusculas
    else:
        return minusculas

# Utilizamos la función anidada
print(hablar(0.6)('Hablo fuerte'))
print(hablar(0.3)('Hablo suave'))

variable_minusculas = hablar(0.4)
print(variable_minusculas('hablo suave nuevamente'))

####################
# Closures
# Las funciones internas pueden capturar y guardar el estado de la función externa
def hablar(texto, volumen):
    # La función interna ya no recibe parámetros
    # Utiliza el estado de la función padre (externa)
    def minúsculas():
        return texto.lower()
    def mayúsculas():
        return texto.upper()
    if volumen > 0.5:
        return mayúsculas()
    else:
        return minúsculas()

print(hablar('hablo fuerte...', 0.8))
print(hablar('hablo suave...', 0.3))

# Otro ejemplo de closure
# Podemos preconfigurar una función
def mostrar(titulo):
    # Definimos la función anidada
    def saludar(mensaje):
        return titulo + '. ' + mensaje
    return saludar

mostrar_ing = mostrar('Ingeniero')
mostrar_lic = mostrar('Licenciado')
# Podemos seguir usando el estado de la función previamente configurada
# aunque el valor del título ya esté fuera del alcance (scope)
print(mostrar_ing('Alvaro Ruiz'))
print(mostrar_lic('Carlos Esparza'))

############################
# La funcipón callable nos permite saber si un objeto se puede llamar o no
# No todos los objetos son funciones
print(f'Se puede llamar el objeto mostrar como función?: {callable(mostrar)}')
print(f'Se puede llamar el objeto hablar como función?: {callable(hablar)}')
print(f'Se puede llamar el objeto mostrar_ing como función?: {callable(mostrar_ing)}')
print(f'Se puede llamar el objeto str como función?: {callable("cualquier texto")}')

# Si queremos que una clase defina objetos que se puedan llamar como funciones
# tenemos que sobreescribir el método __call__
class Mostrar:
    def __init__(self, titulo):
        self.titulo = titulo

    def __call__(self, mensaje):
        return self.titulo + '. ' + mensaje

mostrar_doctor = Mostrar('Doctor')
print(mostrar_doctor('Carlos Ugalde'))
print(f'Se puede llamar el objeto mostrar_doctor como una función?: {callable(mostrar_doctor)}')












