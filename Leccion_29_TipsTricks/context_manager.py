from contextlib import contextmanager

# Forma sintética
# with open('prueba.txt') as archivo:
#     archivo.write('hola desde Python')

# Esto es equivalente a:
# archivo = open('prueba.txt','w')
# try:
#     archivo.write('hola desde Python')
# finally:
#     archivo.close()

# Esto NO es equivalente
# archivo = open('prueba.txt','w')
# archivo.write('hola sin with')
# # Esto no asegura el cierre de recursos en caso de error
# archivo.close()

# MAnejo de Context Manager en Clases
# 1. Implementando el protocolo con las funciones (__enter__) y (__exit__)
# 2. Utilizando la libreria de contextlib

# Opción 1



class ManejoArchivos:
    def __init__(self, nombre,modo):
        self.nombre = nombre
        self.modo = modo

    def __enter__(self):
        self.archivo = open(self.nombre, self.modo)
        return self.archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.archivo:
            self.archivo.close()

# Este métodoes un generador, en primer lugar adquiere el recurso
# posteriormente suspende temporalmente la ejecución al utilizar yield
# Una vez utilizado, regresa a la ejecución y cierra el recurso
@contextmanager
def manejador_archivos(nombre, modo):
    try:
        archivo = open(nombre,modo)
        yield archivo
    finally:
        archivo.close()

# Ejercicio de Identador
class Identador():
    def __init__(self):
        self.nivel = 0

    def __enter__(self):
        self.nivel += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.nivel = -1

    def imprimir(self, texto):
        print(' ' * self.nivel + texto)

# Mismo ejercicio identador con contextlib
class Identador2():
    def __init__(self):
        self.nivel = 0

    @contextmanager
    def identar(self):
        try:
            self.nivel += 1
            yield self
        finally:
            self.nivel -= 1

    def imprimir(self, texto):
        print(' ' * self.nivel + texto)


if __name__ == '__main__':
    # Prueba implementando el protocolo de Context Manager
    with ManejoArchivos('prueba.txt','w') as archivo:
        archivo.write('Context Manager')

    # Prueba con la biblioteca contextlib
    with manejador_archivos('prueba.txt','w') as archivo:
        archivo.write('prueba desde decorador')
        archivo.write('\nadios')

    # Prueba de Identador
    with Identador() as identador:
        identador.imprimir('primer nivel')
        with identador:
            identador.imprimir('segundo nivel')
            identador.imprimir('continua segundo nivel...')
            with identador:
                identador.imprimir('tercer nivel')
                identador.imprimir('continua tercer nivel...')
        identador.imprimir('fin primer nivel')

    # Prueba de Identador2
    print()
    objeto = Identador2()

    with objeto.identar():
        objeto.imprimir('primer nivel')
        with objeto.identar():
            objeto.imprimir('segundo nivel')
            objeto.imprimir('continuar segundo nivel...')
            with objeto.identar():
                objeto.imprimir('tercer nivel')
                objeto.imprimir('continuar tercer nivel...')
        objeto.imprimir('fin de primer nivel')