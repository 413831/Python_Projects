# nota:primero debe estar declarada para llamarla
def mi_funcion(nombre, apellido):
    print('saludos desde mi funcion')
    print(f'Nombre: {nombre}, Apellido: {apellido}')

# el tipo de dato de retorno es a modo de guía y opcional
# se pueden definir argumentos por default
def sumar(a = 0, b = 0) -> int:
    return a + b

# argumentos variables
# internamente se genera una tupla del parámetro
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


def listarTerminos(nombre, *nombres, **terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['Juan','Karla','Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres((10,11))



