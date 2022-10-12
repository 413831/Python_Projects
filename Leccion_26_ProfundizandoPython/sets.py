# Profundizando en Set
# Un set es una colección de elementos únicos y es mutable
# Los elementos de un set deben ser inmutables
conjunto = {'Juan','True',2,18.0}

# set vacío correcto
conjunto = set()

# Mutable
conjunto.add('Juan')
print(conjunto)

# Contiene valores únicos
conjunto.add('Juan')
print(conjunto)

# Crear un set a partir de un iterable
conjunto = set([4,5,7,8,4])
print(conjunto)

# Podemos agregar más elementos o incluso otro set
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

# Copiar un set (copia poco profunda, solo se copian las referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# Verificar igualdad
print(f'Es igual en contenido? {conjunto == conjunto_copia}')
print(f'Es la misma referencia? {conjunto is conjunto_copia}')

# Operaciones de conjuntos con set :)
# Personas con distintas características
pelo_negro = {'Juan','Karla','Pepito','Maria'}
pelo_rubio = {'Kevin','Laura','Marcos'}
ojos_cafe = {'Karla','Laura','Juan'}
menores_30 = {'Juan','Karla','Maria'}

# Union - Todos los elementos con ojos color cafe y pelo rubio
# nota: es una operacion conmutativa
print(ojos_cafe.union(pelo_rubio))
# Invertir el orden con el mismo resultado
print(f'Union: {pelo_rubio.union(ojos_cafe)}')

# Intersection (AND) - Sólo las personas con ojos café y pelo rubio
# nota: operacion conmutativa
print(f'Intersection: {ojos_cafe.intersection(pelo_rubio)}')

# Difference - Pelo negro sin ojos cafe
# nota: no es operacion conmutativa
print(f'Difference: {pelo_negro.difference(ojos_cafe)}')

# Symmetric Difference (XOR)
# nota: operacion conmutativa
print(f'Symmetric difference: {pelo_negro.symmetric_difference(ojos_cafe)}')

# Subset - Preguntar si un set está contenido en otro
# Revisamos si los elementos del primer set están contenidos en el segundo set
print(menores_30.issubset(pelo_negro))

# Superset - Preguntar si un set contiene a otro set
# Revisar si los elementos del primer set están contenidos en el segundo set
print(menores_30.issuperset(pelo_negro))

# Disjoint - Preguntar si los elementos de pelo negro no tienen pelo rubio
print(pelo_negro.isdisjoint(pelo_rubio))






