numeros = range(10)
lista_pares = []

# Creamos una nueva lista con los valores pares multiplicados por si mismo
for numero in numeros:
    # Revisamos si es un número par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print(f'Lista pares: {lista_pares}')

# Hacemos lo mismo con list comprehensions
# [expresion for var in colección if condición]
# La condición de if es opcional
lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero % 2 == 0]
print(f'Lista Pares con list comprehensions: {lista_pares}')

# Un ejemplo similar con dos condiciones ( las condiciones son opcionales )
# Solo se agrega el valor a la lista cuando el valor cumple ambas condiciones
# Condiciones: debe ser divisible entre 2 y divisible entre 6
pares = [numero for numero in range(50) if numero % 2 == 0 and numero % 6 == 0]
print(f'Lista divisibles por 2 y 6: {pares}')

# Agregando if else
lista_pares = []
lista_impares = []
for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

# Mismo ejercicio con list comprehension
lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero) for numero in range(10)]
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

# Lista de listas
lista_listas = [[1,2,3],[4,5,6],[7,8,9,10]]
# Convertimos la lista de listas en una sola lista
lista_simple = [valor
                for sublista in lista_listas
                for valor in sublista]
print(f'Lista simple: {lista_simple}')
# Crear una lista de números pares a partir de la lista_listas
# Sin List comprehensions (Ciclos for anidados)
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor % 2 == 0:
            lista_pares.append(valor)
print(f'Lista pares: {lista_pares}')
# Con List comprehensions
lista_pares = []
lista_pares = [valor for sublista in lista_listas for valor in sublista if valor % 2 == 0]
print(f'Lista pares: {lista_pares}')








