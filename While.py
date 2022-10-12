"""# Uso del WHILE en Python
numero = 1 

# Repeticion de numeros
while numero <= 10:
    print(numero)
    numero += 1

# Repeticion de numeros con BREAK
while numero <= 10:
    print(numero)
    if numero == 8:
        break
    numero += 1

# Repeticion de numeros con CONTINUE
numero = 1

while numero <= 10:
    numero += 1
    if numero == 4:
        continue
    print(numero)
"""
# Producto de numeros naturales (factorial)
factor = int(input("introduce un numero natural: "))

factorial = 1
resultado = factorial

while factorial < factor:
    resultado = (factorial + 1) * resultado
    factorial += 1
print(resultado)

