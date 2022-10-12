import psycopg as bd

conexion = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',dbname='test_db')

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Guillermo', 'Ibarra de las nieves', 'gibarradelasnieves@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan Carlos', 'Juarez', 'j.juarez@mail.com', 3)
    cursor.execute(sentencia,valores)

    conexion.commit()
    print('Termina la transacción, se hizo commit')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo rollback: {e}')
finally:
    conexion.close()
    # Se cierra conexión a base de datos
    # cursor.close()