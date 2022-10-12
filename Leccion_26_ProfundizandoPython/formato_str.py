# center - Centrar str
titulo = 'Sitio Web de GlobalMentoring.com.mx'
# print(len(titulo.center(50,'*')))
print(titulo.center(len(titulo) + 10,'*'))

# ljust - alinea a la izquierda
# print(titulo.ljust(50,'*'))
print(titulo.ljust(len(titulo)+10,'-'))

# rjust - alinea a la derecha
# print(titulo.rjust(50,'*'))
print(titulo.rjust(len(titulo)+10,'-'))

# Reemplazar contenido en un str
print(titulo.replace(' ','-'))

# Eliminar caracteres al inicio y final de un str - strip
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original: ',titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada: ',titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.strip('*')
print('Cadena modificada: ',titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada: ',titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada: ',titulo, len(titulo))

titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print('Cadena modificada: ',titulo, len(titulo))