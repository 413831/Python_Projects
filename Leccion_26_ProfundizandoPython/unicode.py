# Caracteres unicode
print('Hola\u0020Mundo')
print('Notación simple:', '\u0041')
print('Notación extendida:', '\U00000041')
print('Notación hexadecimal:','\x41 ')
print('Corazón:','\u2665')
print('Cara sonriendo:','\U0001f600')
print('Serpiente:','\U0001F40D')

# Caracteres ASCII
caracter = chr(65)
print('A Mayúscula:', caracter)
caracter = chr(64)
print('Símbolo @:', caracter)

# Caracteres bytes
caracteres_en_bytes = b'Hola Mundo'
print(caracteres_en_bytes)

mensaje = b'Universidad Python'
print(mensaje[0])
print(chr(mensaje[0]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

# Convertir str a bytes
string = 'Programación con Python'
print('string original:', string)

bytes = string.encode('UTF-8')
print('bytes codificado:', bytes)
# Convertir bytes a str
string2 = bytes.decode('UTF-8')
print('string decodificado:', string2)
print(string == string2)

