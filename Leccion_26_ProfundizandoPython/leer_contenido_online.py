# Leer contenido online
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')]
url = "http://globalmentoring.com.mx/recursos/GlobalMentoring.txt"
# response = opener.open(url)

with opener.open(url) as mensaje:
    contenido = mensaje.read().decode('utf-8')
    print(contenido)

with open('nuevo_archivo.txt','w', encoding='utf-8') as archivo:
    archivo.write(contenido)

# Contar ocurrencias de una cadena
print(contenido.count('Universidad'))

# upper convierte a mayúsculas un str
print(contenido.upper())

# lower convierte a minúsculas un str
print(contenido.lower())

print('Existe python?: ','python'.lower() in contenido.lower())
print('Existe python?: ','python'.upper() in contenido.upper())

# startswith - inicia con
print('Inicia con: ',contenido.startswith('En GlobalMentoring.com.mx '))

# endswith - termina con
print('Termina con: ',contenido.lower().endswith('globalMentoring.com.mx'.lower()))

# Verificar si todos los caracteres de un str estan en minúsculas o mayúsculas
mensaje = 'Hola Mundo'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())

