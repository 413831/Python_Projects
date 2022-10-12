from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    @classmethod
    def generar_id(cls):
        cls.contador_ratones += 1
        return cls.contador_ratones

    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        self._id_raton = Raton.generar_id()

    def __str__(self):
        return f'Raton id: {self._id_raton}, Marca: {super().marca}, Tipo entrada: {self.tipo_entrada}'
