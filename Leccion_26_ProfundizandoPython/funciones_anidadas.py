# Funciones Anidadas

def calculadora(a, b, operacion='sumar'):
    # 1. Definición de funcion anidada
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    # 2. Llamado a la funcion anidada
    if operacion == 'sumar':
        print(f'Resultado sumar: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado restar: {restar(a, b)}')

calculadora(5 , 6)
calculadora(6,3,operacion='restar')