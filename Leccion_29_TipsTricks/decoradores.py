# Los decoradores permiten extender y modificar el comportamiento de las funciones
# Se ejecuta la lógica del decorador en tiempo de ejecución
# Ejemplos comunes: logging, seguridad, caching
# Un decorador es código reutilizable

# Primer ejemplo
def decorador_envolvente(funcion_a_decorar):
    # Recibir la función y regresarla
    print('Estamos dentro de la función decoradora')
    return funcion_a_decorar

# Ahora utilicemos este decorador
def saludar():
    return 'Saludos desde mi función...'

# Llamamos manualmente el decorador (NO es lo comun)
funcion_retornada = decorador_envolvente(saludar)
print(funcion_retornada)

@decorador_envolvente
def saludar_funcion_a_decorar():
    return 'Saludos desde función a decorar...'

print(saludar_funcion_a_decorar())

# Decorador que convierte el texto a mayúsculas
def mayusculas(funcion_a_decorar):
    def envolvente():
        # Mandamos a llamar la funcion original (closure)
        print('Codigo antes de la llamnada a la funcion a decorar')
        resultado_original = funcion_a_decorar()
        print('Codigo luego de la llamnada a la funcion a decorar')
        resultado_modificado = resultado_original.upper()
        return resultado_modificado
    return envolvente

@mayusculas
def saludar_minusculas():
    return 'hola mundo'

print(saludar_minusculas())

##########################
# Decoradores múltiples
# <strong><em>Hola</em></strong>
def negritas(funcion):
    def funcion_envolvente():
        return '<strong>' + funcion() + '</strong>'
    return funcion_envolvente

def enfatizar(funcion):
    def funcion_envolvente():
        return '<em>' + funcion() + '</em>'
    return  funcion_envolvente

# nota: se ejecutan del mas interno hacia el mas externo (from bottom to top)
@negritas
@enfatizar
def saludar_html():
    return 'Hola con HTML'

print(saludar_html())

################
# Decoradores con Argumentos
# *args y **kwargs
def decorador_con_argumentos(funcion):
    def función_envolvente(*args, **kwargs):
        print('Se está ejecutando el decorador')
        print('args',args)
        print('kwargs',kwargs)
        # Modificar los argumentos antes de evnviarlos
        lista_arg = []
        for indice, valor_tupla in enumerate(args):
            lista_arg.append(args[indice].upper())
        # Agregamos más elementos a la lista
        lista_arg.append('nuevo arg 1')
        lista_arg.append('nuevo arg 2')
        # Agregamos información al diccionario
        kwargs['valor1'] = 'Nuevo valor 1'
        kwargs['valor2'] = 'Nuevo valor 2'
        # Propagamos los parámetros a la función original
        # return funcion(*args, **kwargs)
        return funcion(*lista_arg, **kwargs)
    return función_envolvente

@decorador_con_argumentos
def funcion_saludar(titulo, nombre, *args, **kwargs):
    # Imprimir título con el nombre
    print(f'{titulo}. {nombre}')
    # Imprimimos los argumentos variables
    print('args: ',args)
    print('kwargs: ', kwargs)

funcion_saludar('Ingeniera','María Quiróz')


