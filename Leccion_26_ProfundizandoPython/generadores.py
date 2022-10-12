# Generadores
# Es una función especial, retorna una secuencia de valores
# Suspende la ejecución de la función con yield (producir)
# No se usa return

def generador():
    yield 1
    print('Se reanuda la ejecución')
    yield 2
    print('Se reanuda la ejecución')
    yield 3

# Consumir el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))

# Si tratamos de consumir más valores de los que produce el generador
# lanza un error de StopIteration
# print(next(gen))

# Consumiendo los valores del generador con un ciclo for
for valor in generador():
    print(f'Número generado: {valor}')

