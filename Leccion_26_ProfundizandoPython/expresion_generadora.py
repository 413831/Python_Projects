# Expresión generadora (es un generador anónimo)
multiplicación = (valor*valor for valor in range (4))
print(type(multiplicación))
print(next(multiplicación))
print(next(multiplicación))
print(next(multiplicación))
print(next(multiplicación))
# print(next(multiplicación))

# También se puede pasar una expresión generadora a una función (sin paréntesis)
import math

suma = sum(valor * valor for valor in range(4))
print(f'Resultado suma: {suma}')

# También podemos usar una lista o cualquier otro iterador
lista = ['Juan','Jose','Pepe']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

# Crear un string a partir de un generador creado a partir de lista
lista = ['Karla','Gomez']
contador = 0

# Definimos una función para incrementar el contador
def incrementar():
    global contador
    contador += 1
    return contador
# La primera parte es el yield, la segunda parte es el for, entre paréntesis
generador = (f'{incrementar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'Cadena generada: {cadena}')


