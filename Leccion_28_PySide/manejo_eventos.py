import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.setFixedSize(400,200)
        # Definimos la etiqueta y línea de edición
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        # Conectar el widget de entrada_texto con la etiqueta
        # la señal es textChanged, el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # Publicamos los componentes usando un vertical box layout
        cuadro = QVBoxLayout()
        cuadro.addWidget(self.entrada_texto)
        cuadro.addWidget(self.etiqueta)
        # Crear un contenedor
        contenedor = QWidget()
        contenedor.setLayout(cuadro)
        # Publicamos el contenedor
        self.setCentralWidget(contenedor)



        # Boton
        # self.boton = QPushButton('Click aquí')
        # Asociamos la señal de click al slot evento_click
        # self.boton.clicked.connect(self.evento_click)

        # Conectamos el evento seleccionado (por default es False)
        # boton.setCheckable(True)
        # # Conectamos otro slot al evento check
        # boton.clicked.connect(self.evento_check)
        # # Conectamos el evento click (signal) con el slot (evento_click)
        # boton.clicked.connect(self.evento_click)
        # Conectar a la señal de cambio de título
        # self.windowTitleChanged.connect(self.cambio_titulo_ventana)

        # Publicamos el botón
        # self.setCentralWidget(self.boton)

    def evento_click(self):
        # Cambiar el texto del botón y el título de la ventana
        self.boton.setText('Nuevo texto botón')
        self.boton.setEnabled(False)
        self.setWindowTitle('Nuevo título de la Aplicación')

    def cambio_titulo_ventana(self, nuevo_titulo):
        print(f'Nuevo título aplicación: {nuevo_titulo}')


    # def evento_check(self, check):
    #     self.boton_seleccionado = check
    #     print('CHECADO?', self.boton_seleccionado)
    #     # Accedemos al estado del botón (checked)
    #     print('Botón seleccionado desde evento click?', self.boton_seleccionado)
    #
    #
    # # Creamos el método (slot) que procesa o consume el evento (signal)
    # def evento_click(self):
    #     print('Has hecho click')


if __name__ == '__main__':
    # Creamos el objeto aplicación
    app = QApplication()
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
