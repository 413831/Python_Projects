class Monitor:
    contador_monitores = 0

    @classmethod
    def generar_id(cls):
        cls.contador_monitores += 1
        return cls.contador_monitores

    def __init__(self, marca, tamaño):
        self._id_monitor = Monitor.generar_id()
        self._marca = marca
        self._tamanio = tamaño

    def __str__(self):
        return f'Monitor id: {self._id_monitor}, Marca {self._marca}, Tamaño {self._tamanio}'


    @property
    def id_monitor(self):
        return self._id_monitor

    @id_monitor.setter
    def id_monitor(self, id_monitor):
        self._id_monitor = id_monitor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

if __name__ == '__main__':
    monitor1 = Monitor('HP',15)
    print(monitor1)