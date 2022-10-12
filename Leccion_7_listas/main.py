# Definir una lista de tipo str
nombres = ['Juan','Carla','Ricardo','Jose Luis','Maria']
# imprimir la lista nombres
print(nombres)
# acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])
# acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
# Imprimir un rango
print(nombres[0:2])
# acceder desde el inicio de la lista al indice sin incluirlo
print(nombres[:3])
# acceder desde el indice hasta el final
print(nombres[1:])
# Iterar lista
for nombre in nombres:
    print(nombre)

# Agregar un elemento
nombres.append('Lorenzo')
# Insertar un elemento en un indice
nombres.insert(1,'Octavio')
# Remover un elemento
nombres.remove('Octavio')
# Remover el ultimo valor de la lista
nombres.pop()
print(nombres)
# eliminar un índice
del nombres[0]
print(nombres)

