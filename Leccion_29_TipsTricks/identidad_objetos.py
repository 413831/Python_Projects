# Comparación del uso de operador == o el operador is en POO

# El operador == compara el contenido de 2 objetos (contenido igual)
# no necesariamente son el mismo objeto (pueden apuntar a objetos distintos)

# Operador is revisa si dos objetos son iguales (objetos son idénticos)
# Ambos deben estar apuntando a la misma dirección de memoria para ser igual

# Ejemplo de una lista
lista_a = [1,2,3]
lista_b = lista_a

# En este caso tanto la lista a y b tienen el mismo contenido (== es True)
# y también apuntan a la misma referencia (is regresa True)
print(f'Lista a y b tienen el mismo contenido?: {lista_a == lista_b}')
print(f'Lista a y b apuntan al mismo objeto:? {lista_a is lista_b}')

lista_c = list(lista_a)
# Mismo contenido (== True)
# Distinas referencias (is regresa False)
print(f'Lista a y c tienen el mismo contenido?: {lista_a == lista_c}')
print(f'Lista a y c apuntan al mismo objeto?: {lista_a is lista_c}')