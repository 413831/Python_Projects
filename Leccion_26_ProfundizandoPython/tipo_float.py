# Profundizando tipo float
a = 3.0
# Constructor float puede recibir int y str
a = float(10)
a = float('12')
print(f'a: {a:.3f}')
# Notacion exponencial (valores positivos o negativos)
a = 3e5
a = 3e-5
print(f'a :{a:.10f}')
# Cualquier cálculo que involucre un float, se promueve a float
a = 4.0 + 5
print(a)
print(type(a))



