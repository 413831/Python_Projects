# Leer contenido online
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')]
url = "http://globalmentoring.com.mx/recursos/GlobalMentoring.txt"
# response = opener.open(url)

palabras = []
with opener.open(url) as mensaje:
    for linea in mensaje:
        palabras_por_linea = linea.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)

print(palabras)