# Un closure es una función que define a otra, y ademas la puede regresar
# La función anidada puede acceder a las variables locales definidas en la funcion principal o externa

# Función principal

# def operacion(a, b):
#     # Definimos una función interna o anidada
#     def sumar():
#         return a + b
#
#     # Retornar la función
#     return sumar

#  Función principal
def operacion(a, b):
    # 1. Definimos función lambda interna o anidada y la retornamos
    return lambda: a + b


mi_funcion_closure = operacion(5, 2)
print(f'Resultado de la función closure: {mi_funcion_closure()}')

# Llamado a la función regresada al vuelo
print(f'Resultado de la función closure ejecutada al vuelo: {operacion(2,3)()}')

