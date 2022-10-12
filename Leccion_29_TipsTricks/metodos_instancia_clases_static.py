# Metodos de instancia, clase y static y sus diferencias
class MiClase:
    def metodo_instancia(self):
        # Retornamos una tupla
        return 'Método de instancia ejecutado...', self

    @classmethod
    def metodo_clase(cls):
        # Retornar una tupla
        return 'Metodo de clase ejecutado...',cls

    @staticmethod
    def metodo_estático():
        # Se conocen como métodos de utileria
        return 'Método estático ejecutado...'

# Caso 1. Ejecutamos el método de instancia
objeto = MiClase()
print(objeto.metodo_instancia())

# Caso 2. Ejecutamos el método de instancia de manera explícita
print(MiClase.metodo_instancia(objeto))

# Caso 3. Ejecutamos el método de instancia desde la clase
print(MiClase.metodo_instancia(MiClase))

# Caso 4. Ejecutamos el método de clase
print(MiClase.metodo_clase())

# Case 5. Desde las instancias podemos acceder a los métodos de clase
print(objeto.metodo_clase())

# Caso 6. Ejecutamos el método estático
print(MiClase.metodo_estático())

# Caso 7. Ejecutamos el método estático desde la instancia
print(objeto.metodo_estático())
