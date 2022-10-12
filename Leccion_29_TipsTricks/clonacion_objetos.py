import copy

# Clonación (copia) de objetos
# Copia superficial (shallow) o copia poco profunda
lista_a = [[1,2],[3,4],[5,6]]
# Ejemplo 1.
# Dos objetos distintos en primer nivel, diferente posicion de memoria
# En el segundo nivel se copian las referencias
lista_b = list(lista_a)

print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')
# Comprobación de que los objetos son distintos
# Un cambio en el nivel superior, no afecta a la otra lista
lista_a.append([7,8])
print('Son distinto objetos (nivel superior)')
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')
# Comprobación de que los objetos internos tienen la misma referencia
# Un cambio en un elemento de una sublista, afecta a la sublista de la otra lista
lista_a[0][1]='A'
print(f'La copia fue superficial, de los elementos internos sólo se copiaron las referencias')
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')
##############################
# Crear copias profundas (import copy)
lista_c = [[1,2],[3,4],[5,6]]
lista_d = copy.deepcopy(lista_c)
# Comprobación de que son objetos distintos
lista_c.append([7,8])
print(f'Son distintos objetos (nivel superior)')
print(f'Lista c: {lista_c}')
print(f'Lista d: {lista_d}')
# Ahora si, los elementos internos son nuevos objetos, no solo se copió la referencia
lista_c[0][1]='A'
print(f'Lista c: {lista_c}')
print(f'Lista d: {lista_d}')
# El método copy sirve para realizar copias
