# Las funciones en Python son ciudadanas de primera clase
# First Class Citizens

# Definimos la funcion
def sumar(a, b):
    return a + b

# 1. Asignar función a una variable (no se usan paréntesis)
mi_funcion = sumar

# Verificar tipo de la variable
print(type(mi_funcion))

# Llamado a la función por medio de la variable
resultado = mi_funcion(7,3)
print(f'Resultado de mi funcion: {resultado}')

# 2. Función como argumento
def operar(a, b, sumar_arg):
    print(f'Resultado: {sumar_arg(a, b)}')

operar(4, 5, sumar)

# 3. Retornar función
def retornar_funcion():
    # Retornamos una función
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'Resultado función retornada: {mi_funcion_retornada(1,5)}')