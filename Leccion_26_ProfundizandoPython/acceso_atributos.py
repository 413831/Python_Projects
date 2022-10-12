# Ejemplo atributos públicos, protegidos, privados
class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

objeto = MiClase('Valor público', 'Valor protegido','Valor privado')
# Acceso al atributo público
print(objeto.publico)
# Modificar el valor público
objeto.publico = 'Nuevo valor público'
print(objeto.publico)

# Acceso al valor protegido
print(objeto._protegido) #NO ES BUENA PRÁCTICA

# Modificar atributo protegido
objeto._protegido = 'Nuevo valor protegido' #NO ES BUENA PRÁCTICA
print(objeto._protegido)

# Acceder al valor privado
print(objeto._MiClase__privado) #NO ES BUENA PRÁCTICA
# Modificar valor privado
objeto._MiClase__privado = 'Nuevo valor privado'
print(objeto._MiClase__privado)