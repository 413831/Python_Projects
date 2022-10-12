import json
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')]
url = 'http://www.globalmentoring.com.mx/api/clima.json'

with opener.open(url) as mensaje:
    cuerpo_respuesta = mensaje.read()
    # print(cuerpo_respuesta)

    json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
    # print(json_respuesta)

    # Ejercicio 1. Acceder a la descripción del clima
    descripcion_clima = json_respuesta.get('clima')[0].get("descripcion")
    print(f'Descripción clima: {descripcion_clima}')

    # Ejercicio 2. Mostar la temparatura mínima y máxima
    temp_min = json_respuesta.get('principal').get('temp_min')
    print(f'Temperatura mínima: {temp_min}')
    temp_max = json_respuesta.get('principal').get('temp_max')
    print(f'Temperatura máxima: {temp_max}')
