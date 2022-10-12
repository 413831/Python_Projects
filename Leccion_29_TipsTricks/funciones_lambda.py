# Las funciones lambda nos permiten declarar funciones anónimas es una sola lines
# Ejemplo normal
def sumar(a, b):
    return a + b

print(sumar(3, 5))

# Funcion lambda
sumar_lambda = lambda a, b: a + b
print(sumar_lambda(2, 4))

# Utilizando una sola línea de código
print((lambda a, b: a + b)(5, 6))

# Podemos usar una función lambda siempre que necesitemos una función concreta
# Ej. Ordenar una lista de tuplas, por su segundo valor proporcionando una llave (key)
lista_tuplas = [(1,'b'),(2,'f'),(5,'a'),(4,'c')]
# lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[0], reverse=True)
lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[1])
print(lista_tuplas_ordenada)

# Otro ejemplo de ordenamiento usando una expresión lambda
print(list(range(-3,4)))
# Si queremos ordenar por el valor absoluto (sin considerar signo)
for valor in range(-3,4):
    print(valor, valor*valor)

# Ahora lo aplicamos a una expresión lambda
lista_ordenada = sorted(range(-3,4), key=lambda valor: valor*valor)
# Se ordenan por el valor absoluto
print(lista_ordenada)

# Las funciones lambda también podemos aplicar el concepto de closure
def mostrar(título):
    return lambda mensaje: título + '. ' + mensaje

mostrar_ing = mostrar('Ingeniero')
mostrar_lic = mostrar('Licenciado')
print(mostrar_ing('Carlos Lara'))
print(mostrar_lic('Armando Casas'))

# Ejemplos de casos de funciones lambda NO recomendables
class Prueba:
    mostrar = lambda self: print('Función mostrar')
    saludar = lambda self: print('Función saludar')

prueba = Prueba()
prueba.mostrar()
prueba.saludar()

# Otro ejemplo donde una función lambda agregaria complejidad innecesaria
lista_pares = list(filter(lambda valor: valor % 2 == 0, range(10)))
print(lista_pares)
# Ejemplo correcto con list comprehensions
lista_pares_modificada = [valor for valor in range(10) if valor % 2 == 0]
print(lista_pares_modificada)








