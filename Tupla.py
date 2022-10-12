# Como usar tuplas en Python
nombres = ("carlos","pepito","heraclito","ramona")
numeros = (1,2,2,2,5,)
booleanos = (True,False,True)
combinacion = ("laurencio", True, 123)

print(nombres)
print(numeros)
print(booleanos)
print(combinacion)

print(len(nombres))

# Acceder a elementos de una tupla
print(nombres[2])
print(nombres[0:2])
print(nombres[-1])

# Actualizar una tupla
lista = list(nombres)
lista[1] = "Oscar"
nombres = tuple(lista)
print(nombres)

# Desempaquetar una tupla
(uno, dos, tres, cuatro, cinco) = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)

# Metodos count(), index()
# Cuenta la cantidad del valor indicado dentro de la tupla
print(numeros.count(2))
# Retorna el indice del valor indicado
print(numeros.index(5))





