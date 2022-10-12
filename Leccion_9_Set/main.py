# set
planetas = {'Marte','Júpiter','Venus'}
print(planetas)

# Largo
print(len(planetas))

# Revisar si el elemento está presente
print('Marte' in planetas)

if 'Júpiter' in planetas:
    print("Júpiter existe")
# nota: en un Set no se pueden duplicar elementos
planetas.add('Tierra')
planetas.add('Tierra')
print(planetas)

# Eliminar elementos
planetas.remove('Tierra')
print(planetas)
planetas.discard('Júpiter') # se elimina de forma segura sin error
print(planetas)

# Limpiar Set
planetas.clear()
print(planetas)

# Eliminar Set
del planetas
print(planetas)
