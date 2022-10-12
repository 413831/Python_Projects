# Leer archivo json
# JSON = Javascript Object Notation
import json
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')]
url = 'http://www.globalmentoring.com.mx/api/personas.json'

with opener.open(url) as mensaje:
    cuerpo_respuesta = mensaje.read()
    # Procesamos la respuesta
    json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
    print(json_respuesta)

# Imprimir sólo los nombres de las personas
# JSON se convierte a listas y diccionarios en python
for persona in json_respuesta['personas']:
    print(f'Persona: {persona["nombre"]} {persona["edad"]}')
# Accedemos a las variables independientes
print(f'Total de personas: {json_respuesta["total"]}')
print(f'Mensaje: {json_respuesta["mensaje"]}')

