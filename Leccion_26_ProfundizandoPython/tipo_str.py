# Profundizando en el tipo str
from mi_clase import MiClase

# Concatenación automática en python
variable = 'Adios'
mensaje = 'Hola' 'Mundo' + variable
mensaje += 'Universidad' 'Python'

'''
help(int)
help(str.capitalize)
help(MiClase)
print(MiClase.__doc__)
print(MiClase.__init__.__doc__)
print(MiClase.mi_metodo.__doc__)
print(MiClase.mi_metodo)
print(type(MiClase.mi_metodo))
'''
'''
comentario
varias
lineas
'''

help(str.capitalize)
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()
print(f'mensaje1: {mensaje1}, id{hex(id(mensaje1))}')
print(f'mensaje2: {mensaje2}, id{hex(id(mensaje2))}')
mensaje1 += 'adios'
print(f'mensaje1: {mensaje1}, id{hex(id(mensaje1))}')

tupla_str = ('Hola', 'Mundo','Universidad','Python')
mensaje = ' '.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_cursos = ['Java','Python','Angular','Spring']
mensaje = ', '.join(lista_cursos)
print(f'mensaje: {mensaje}')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'mensaje: {mensaje}')

diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': '18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
# print(f'llaves: {llaves}')
# print(f'valores: {valores}')

# Split
cursos = 'Java Python JavaScript Angular Spring Excel'
# nota: el separador por defecto es el espacio
lista_cursos = cursos.split()
# print(f'lista cursos: {lista_cursos}')
# print(type(lista_cursos))

cursos_separados_coma = 'Java,Python,Java,Angular,Spring,Excel'
lista_cursos = cursos_separados_coma.split(',')
# print(f'lista cursos: {lista_cursos}')
# print(len(lista_cursos))

lista_cursos = cursos_separados_coma.split(',',2)
# print(f'lista cursos: {lista_cursos}')
# print(len(lista_cursos))

# Parametros posicionales de str
nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre, edad)
# print(mensaje_con_formato)

persona = ('Karla','Gomez',5000)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'%persona
# print(mensaje_con_formato)

mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
# print(mensaje_con_formato%persona)

# Metodo Format de str

mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
# print(mensaje_con_formato)

mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)

mensaje = 'Sueldo {2:.2f} Nombre {0} Edad {1} '.format(nombre, edad, sueldo)
# print(mensaje)

mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre,e=edad,s=sueldo)
# print(mensaje)

diccionario = {'nombre':'Ivan', 'edad':35, 'sueldo':8000.00}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}'.format(dic=diccionario)
# print(mensaje)

# F-string
# interpolacion
mensaje = f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'
print(mensaje)

# Metodo print
print(nombre, edad, sueldo, sep=', ')

