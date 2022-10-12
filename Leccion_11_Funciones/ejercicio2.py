def imprimirNumeros(numero):
    if numero >= 1:
        print(numero)
        imprimirNumeros(numero - 1)

def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32


def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# Llamado a funciones

# imprimirNumeros(5)

celsius = int(input("Ingrese el valor de grados celsius\n"))
resultado = celsius_fahrenheit(celsius)
print(resultado)

fahrenheit = fahrenheit_celsius(resultado)
print(fahrenheit)