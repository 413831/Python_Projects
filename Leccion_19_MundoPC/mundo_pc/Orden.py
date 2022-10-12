class Orden:
    contador_ordenes = 0

    @classmethod
    def generarId(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, computadoras):
        self._id_orden = Orden.generarId()
        self._computadoras = list(computadoras)

    def agregar_computadora(self, computadora):
        if computadora not in self._computadoras:
            self._computadoras.append(computadora)

    def __str__(self):
        detalle_computadoras = ''
        for computadora in self._computadoras:
            detalle_computadoras += computadora.__str__()
        return f'''
        Orden: {self._id_orden} 
        Computadoras: {detalle_computadoras}'
        '''

    @property
    def id_orden(self):
        return self._id_orden

    @id_orden.setter
    def id_orden(self, id_orden):
        self._id_orden = id_orden

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self,computadoras):
        self._computadoras = computadoras

