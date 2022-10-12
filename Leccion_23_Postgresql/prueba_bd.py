import psycopg as bd

conexion = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',dbname='test_db')

#print(conexion)
# Se recupera cursor para comandos SQL
# cursor = conexion.cursor()

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Andres', 'Paz', 'a.paz@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Mariela', 'Arana', 'm.arana@mail.com', 3)
            cursor.execute(sentencia, valores)
except Exception as e:
    print(f'Ocurrió un error, se hizo rollback: {e}')
finally:
    conexion.close()
    # Se cierra conexión a base de datos
    # cursor.close()
print('Termina la transacción, se hizo commit')

# -- EJEMPLOS
# sentencia = 'SELECT * FROM personas WHERE id_persona = %s'

# sentencia = 'SELECT * FROM personas WHERE id_persona = ANY(%s)' # No se utilizan tuplas de tuplas en psycopg3
# # llaves_primarias = [[1,2,3]]
'''
    entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
    llaves_primarias = [entrada.split(',')]
    print(llaves_primarias)
    cursor.execute(sentencia, llaves_primarias) # Se ejecuta QUERY a table
    registros = cursor.fetchall() # Se recuperan los registros de la QUERY
    for registro in registros:
       print(registro)
'''

# sentencia = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
#             valores = ('Carlos','Lara','clara@mail.com')

# sentencia = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
#             valores = (
#                 ('Maria','Lopez','mlopez@mail.com'),
#                 ('Hermeneguildo', 'Herz', 'h.hmail@mail.com'),
#                 ('Angel', 'Quintana', 'aquintana@mail.com')
#             )
#             cursor.executemany(sentencia,valores)

# sentencia = 'UPDATE personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
#             valores = (
#                 ('Patricio', 'Pereyra', 'p.pereyra@mail.com', 1),
#                 ('Ivan', 'Navi', 'i_navi@mail.com', 2)
#             )

#sentencia = 'DELETE FROM personas WHERE id_persona = ANY(%s)'
# entrada = input('Proporciona los id_persona para eliminar (separado por comas): ')
# llaves_primarias = entrada.split(',')
# cursor.executemany(sentencia,[[llaves_primarias]])