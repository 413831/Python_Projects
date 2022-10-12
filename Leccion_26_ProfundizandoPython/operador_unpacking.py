# * desempaquetar
numeros = [1,2,3]
print(numeros)
# Operador unpacking
print(*numeros)
print(*numeros, sep=' - ')

# Desempaquetando al momento de pasar un parámetro a una función
def sumar(a, b, c):
    print(f'Resultado suma: {a + b + c}')


sumar(*numeros)

# Extraer algunas partes de una lista
mi_lista = [1,2,3,4,5,6]
a, *b, c, d = mi_lista
print(a, b, c, d)

# Unir lista
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1,lista2]
print(f'Lista de listas: {lista3}')
lista3 = [*lista1, *lista2]
print(f'Unir listas: {lista3}')

# Unir diccionarios
dict1 = {'A':1,'B':2,'C':3}
dict2 = {'D':4,'E':5}
dict3 = {**dict1, **dict2}
print(f'Unir diccionarios: {dict3}')

# Construir una lista a partir de un str
lista = [*'HolaMundo']
print(lista)
print(*lista, sep='')











