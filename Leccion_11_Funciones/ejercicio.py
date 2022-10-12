# Definiciones de funciones
def sumarizar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


def multiplicar_valores(*numeros):
    total = 1
    for numero in numeros:
        total *= numero
    return total


# Llamado a funciones
resultado = multiplicar_valores(1,2,3)
print(resultado)