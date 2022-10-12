import os

class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    def __init__(self):
        pass

    @staticmethod
    def agregar_peliculas(pelicula):
        with open(CatalogoPeliculas.ruta_archivo,'a',encoding='utf8') as catalogo:
            catalogo.write(f'{pelicula.nombre}\n')


    @staticmethod
    def listar_peliculas():
        try:
            with open(CatalogoPeliculas.ruta_archivo, 'r', encoding='utf8') as catalogo:
                print('LISTADO'.center(50,'-'))
                print(catalogo.read())
        except FileNotFoundError as fe:
            print(f'Error: {fe}')

    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
        except FileNotFoundError as fe:
            print(f'Error: {fe}')

