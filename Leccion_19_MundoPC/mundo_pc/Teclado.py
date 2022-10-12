from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contador_teclados = 0

    @classmethod
    def generar_id(cls):
        cls.contador_teclados += 1
        return cls.contador_teclados

    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        self._id_teclado = Teclado.generar_id()

    def __str__(self):
        return f'Teclado id: {self._id_teclado}, Marca: {self.marca}, Tipo entrada: {self.tipo_entrada}'

if __name__ == '__main__':
    teclado1 = Teclado('HP','USB')
    print(teclado1)
    teclado2 = Teclado('Genius','USB')
    print(teclado2)