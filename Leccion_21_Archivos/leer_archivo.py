try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    # leer toda la informacion del archivo
    # print(archivo.read())

    # leer algunos caracteres
    # print(archivo.read(5))

    # leer lineas completas
    #print(archivo.readline())

    # iterar archivo
    #for linea in archivo:
    #     print(linea)

    # leer lineas
    # nota: se genera una lista con las lineas del archivo
    #print(archivo.readlines()[2])

    # abrimos un nuevo archivo
    # a - anexar informacion
    archivo2 = open('copia.txt','a')
    archivo2.write(archivo.read())

    archivo.close()
    archivo2.close()

except Exception as e:
    print(e)
finally:
    archivo.close()