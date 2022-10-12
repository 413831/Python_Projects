#Definir una tupla
frutas = ('Naranja','Plátano','Guayaba')

print(frutas)
# Largo de tupla
print(len(frutas))
# Acceder a un elemento
print(frutas[0])
# Navegación inversa
print(frutas[-1])
# Acceder a un rango
print(frutas[0:1])
# nota: si la tupla contiene sólo un elemento se debe finalizar con coma ('Naranja',)
print(frutas[0:2])
# Recorrer elementos
for fruta in frutas:
    print(fruta, end=' ') #Sin salto de linea \n
# Cambiar valor tupla
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print(frutas)
# Eliminar la tupla
del frutas
