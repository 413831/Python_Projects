class MiClase:
    # Variable estática
    variable_clase = 'Valor variable Clase'

    def __init__(self, variable):
        self.variable_instancia = variable

    # Métodos estáticos
    # No acceden a variables de instancia
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls, nombre):
        print(cls.variable_clase)
        print(nombre)

    def metodo_instancia(self):
        self.metodo_clase('Llamado desde metodo de instancia')
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)


MiClase.metodo_clase("Pepito")
objeto = MiClase('variable instancia')
objeto.metodo_instancia()
