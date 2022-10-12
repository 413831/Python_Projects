from ManejoArchivo import ManejoArchivos

# sintaxis par abrir y cerrar archivo
# with open('prueba.txt','r',encoding='utf8') as archivo:
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

# se llaman dos metodos por medio del with
# __enter__ (se abre el recurso)
# __exit__ (se cierra el recurso