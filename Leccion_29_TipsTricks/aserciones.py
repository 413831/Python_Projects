# Tip. Las aserciones nos pueden ayudar a depurar nuestros programas de errores
# que no nos podemos recuperar

# Ejemplo 1. Revisamos si la división es entre 0
def dividir(a, b):
    # Nos aseguramos que el valor de b no es cero para poder continuar
    assert b != 0, 'División entre cero'
    print(f'Resultado división: {a/b}')

# Ejemplo 2. Realizamos el cálculo del promedio de una lista de calificaciones
def obtener_promedio(calificaciones):
    # Si la lista de calificaciones está vacía no debería continuar el programa
    assert len(calificaciones) != 0, 'Lista de calificaciones vacía'
    print(f'El promedio de calificaciones es : {sum(calificaciones)/len(calificaciones)}')

# Ejemplo 3. Realizamos un descuento al producto proporcionado
def aplicar_descuento(productos, descuento):
    precio_con_descuento = productos['precio'] * (1.0 - descuento)
    print(f'Nuevo precio del producto: {precio_con_descuento:0.2f}')
    assert 0 <= precio_con_descuento <= productos['precio'], f'Descuento Inválido {precio_con_descuento:0.2f}'
    print('Descuento válido')



if __name__ == '__main__':
    # Prueba Ejemplo 1. Division entre cero
    dividir(10, 1)
    # Prueba Ejemplo 2. Cálculo de promedio
    calificaciones = [10,7,6,4,7,8,9]
    # calificaciones = []
    obtener_promedio(calificaciones)
    # Prueba Ejemplo 3. Aplicar descuento a un producto
    productos = {'nombre':'Camisa','precio':1500}
    aplicar_descuento(productos,0.2)


