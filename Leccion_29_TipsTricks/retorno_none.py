def funcion1(valor):
    if valor:
        return valor
    else:
        return None

print(funcion1(0))

# De manera implícita se regresa el valor de None
def funcion2(valor):
    if valor:
        return valor

print(funcion2(0))

def funcion3(valor):
    print(valor)
    return None

print(funcion3(10))
