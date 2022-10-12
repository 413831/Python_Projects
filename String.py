# Cadenas de caracteres en Python
nombre = "Heraclito"
texto = """
        Esto
        es 
        un
        texto
        {}
        """
dato = "grande"

# Trabajar con una cadena
for letra in nombre:
    print(letra)

print(len(nombre))

print(nombre * 3)

# Cortar cadenas
print(nombre[0])

print(nombre[len(nombre)- 1])

print(nombre[0:5])

# Cadenas y métodos básicos : upper(), lower(), replace(), formar()
print(nombre.upper())
print(texto.upper())

print(nombre.lower())
print(texto.lower())

print(nombre.replace("cl","z"))
print(texto.replace("texto","wea"))

print(texto.format(dato))


