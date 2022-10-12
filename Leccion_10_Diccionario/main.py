# dict (key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)

# Largo
print(len(diccionario))

# Acceder a un elemento (key)
print(diccionario['IDE'])

# Alternativa para recuperar un elemento
print(diccionario.get('OOP'))

# Modificar un elemento
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

# Iterar los elementos
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# Comprobar si existe elemento
print('IDE' in diccionario)
print('ide' in diccionario)

# Agregar elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# Limpiar diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario
print(diccionario)


