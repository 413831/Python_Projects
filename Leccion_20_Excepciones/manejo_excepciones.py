from NumerosIdenticosException import NumerosIdenticosException
resultado = None


try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    # lanzar una excepción
    if a == b:
        raise NumerosIdenticosException('números idénticos')
    resultado = a /b
except Exception as zde:
    print(f'Ocurrió un error: {zde}')
except TypeError as te:
    print(f'Ocurrió un error: {te}')
except Exception as e: # Tipo más general de excepción
    print(f'Ocurrió un error: {e}')
else:
    # El bloque se ejecuta si ninguna excepción se arrojó
    print('No se arrojó ninguna excepción')
finally:
    # El bloque se ejecuta siempre
    print('Ejecución del bloque finally')


print(f'Resultado: {resultado}')
print('Continuamos...')
