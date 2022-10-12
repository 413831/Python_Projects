# Unpacking - desempaquetado
valores = 1,2,3
print(valores)
print(type(valores))

valor1, valor2, valor3 = 1,2,3
print(valor1, valor2, valor3)

# nota: por convencion el guion bajo (_) se utiliza para variables que no se utilizan
valor1, _,valor3 = 1,2,3
print(valor1, valor3)

# nota: error
# valor1, valor2, valor3 = 1,2,3,4,5,6,7,8,9
print(valor1, valor2, valor3)

valor1, valor2, *valor3, valor4, valor5 = 1,2,3,4,5,6,7,8,9
print(valor1, valor2, valor3, valor4, valor5)
print(type(valor3))

def regresa_varios_datos():
    return 1, 2, 3

# nota: por convencion el astericso con guion bajo (_) se utiliza para variables de retorno que no se utilizan
valor1, *valores_restantes = regresa_varios_datos()
print(valor1, valores_restantes)

hora, separador, minutos = '17:20'.partition(':')
# print(type(variable))
print(hora, separador, minutos)




