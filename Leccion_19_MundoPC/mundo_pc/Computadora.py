from mundo_pc.Monitor import Monitor
from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado


class Computadora:
    contador_computadoras = 0

    @classmethod
    def generar_id(cls):
        cls.contador_computadoras += 1
        return cls.contador_computadoras

    def __init__(self, nombre , monitor, teclado, raton):
        self._id_computadora = Computadora.generar_id()
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''\n
        {self._nombre}: {self._id_computadora}, 
        {self._monitor}, 
        {self._teclado}, 
        {self._raton}'
        '''


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    monitor1 = Monitor('HP', 15)
    raton1 = Raton('Genius','USB')
    computadora1 = Computadora('HP', monitor1,teclado1,raton1)

    print(computadora1)
