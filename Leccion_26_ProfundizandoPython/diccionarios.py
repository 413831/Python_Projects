# Profundizando en diccionarios

# Los diccionarios
diccionario = {'Nombre':'Juan', 'Apellido':'Perez', 'Edad': 28}
print(diccionario)

# Los diccionarios son mutables, pero las llaves deben ser inmutables
# diccionario = {[1,2]:'Valor 1'} ERROR
# diccionario = {(1,2):'Valor1'}
print(diccionario)

# Se agrega una llave si no se encuentra
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario (si ya existe se reemplaza)
diccionario['Nombre'] = 'Juan Carlos'
print(diccionario)

# Recuperar un valor indicando una llave
print(diccionario['Nombre'])
# Si no encuentra la llave lanza una excepcion
# print(diccionario['nombre'])

# Get - Metodo para recuerar llave, si no existe no lanza excepcion
# Se puede configurar valor de retorno si no existe la llave
print(diccionario.get('Nombres','No se encontró la llave'))

# Setdefault - modifica el diccionario en caso de que no encuentr la llave
# Se puede agregar un valor por default
nombre = diccionario.setdefault('Nombres','Valor por default')
print(nombre)
print(diccionario)

# Imprimir con pprint
from pprint import pprint as pp
pp(diccionario, sort_dicts=False)


