# # Crear una clase para definir una  clase de excepción personalizada
# # Ej. Validar que un nombre no pueda tener menos de 3 caracteres
#
# # Este tipo de validación no indica cual es el problema en específico
# def validar(nombre_completo):
#     if len(nombre_completo) < 3:
#         raise ValueError
#     else:
#         print('Validación correcta...')
#
#
# nombre = 'Juan'
# validar(nombre)
#
# # Validación personalizada, indica cual es el problema, y queda autodocumentado
# class NombreDemasiadoCorto(ValueError):
#     pass
#
# def validar_mejorado(nombre_completo):
#     if len(nombre_completo) < 3:
#         raise NombreDemasiadoCorto(nombre_completo)
#
# validar_mejorado('Pi')
class ClaseExcepcionBase(TypeError):
    pass

class NombreDemasiadoCorto(ClaseExcepcionBase):
    pass


def validar_mejorado(nombre_completo):
    if len(nombre_completo) < 3:
        raise NombreDemasiadoCorto(nombre_completo)
    else:
        print('¡Validación correcta!')

nombre = 'Li'
try:
    validar_mejorado(nombre)
except ClaseExcepcionBase as e:
    print(f'{type(e).__name__}, linea {e.__traceback__.tb_lineno} en {__file__}: {e}')