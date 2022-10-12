from abc import ABC

class DispositivoEntrada(ABC):

    def __init__(self, marca, tipo_entrada):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    def __str__(self):
        return f'Dispositivo entrada {self._tipo_entrada}, Marca: {self._marca}'

    @property
    def tipo_entrada(self):
        return self._tipo_entrada

    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,marca):
        self._marca = marca



