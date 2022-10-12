from servicio.CatalogoPeliculas import CatalogoPeliculas
from dominio.Pelicula import Pelicula

opcion = None

while opcion != 4:
    try:
        print('''
        1) Agregar película
        2) Listar películas
        3) Eliminar catálogo de películas
        4) Salir
        ''')
        opcion = int(input('Escribe tu opción: '))

        if opcion == 1:
            nombre_pelicula = input('Escribe nombre de película: ')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_peliculas(pelicula)
            print('Película agregada')
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()
        elif opcion == 3:
            CatalogoPeliculas.eliminar()
            print('Catálogo de peliculas eliminado')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
        opcion = None
else:
    print('Adios!!!')