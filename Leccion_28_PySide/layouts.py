from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, \
    QPushButton, QTabWidget


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente
        self.setPalette(paletaColores)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts en PySide')

        # Creamos el componente tab
        tabulador = QTabWidget()
        # Posición de las etiquetas del tabulador
        tabulador.setTabPosition(QTabWidget.North)
        # Indicamos si queremos que se muevan las etiquetas del tabulador
        tabulador.setMovable(True)
        # Configuracion para MacOs - OPCIONAL
        tabulador.setDocumentMode(True)

        # Agregamos los colores a cada tabulador
        tabulador.addTab(Color('red'), 'Rojo')
        tabulador.addTab(Color('blue'), 'Azul')
        tabulador.addTab(Color('yellow'), 'Amarillo')

        # Creamos los layouts
        # layout_principal = QVBoxLayout()
        # layout_botones = QHBoxLayout()
        # self.layout_tipo_stack = QStackedLayout()
        # # Agregamos los layout hijos al layout principal
        # layout_principal.addLayout(layout_botones)
        # layout_principal.addLayout(self.layout_tipo_stack)
        # # Creamos los botones
        # boton_rojo = QPushButton('Rojo')
        # # Publicar este boton en el layout de botones
        # layout_botones.addWidget(boton_rojo)
        # # Publicamos el color rojo al layout de tipo stack
        # self.layout_tipo_stack.addWidget(Color('red'))
        # # Conectamos el evento pressed del boton respectivo
        # boton_rojo.pressed.connect(lambda: self.activar_tabulador(0))
        #
        # # Creamos botón azul
        # boton_azul = QPushButton('Azul')
        # layout_botones.addWidget(boton_azul)
        # self.layout_tipo_stack.addWidget(Color('blue'))
        # boton_azul.pressed.connect(lambda: self.activar_tabulador(1))
        #
        # # Creamos boton amarillo
        # boton_amarillo = QPushButton('Amarillo')
        # layout_botones.addWidget(boton_amarillo)
        # self.layout_tipo_stack.addWidget(Color('yellow'))
        # boton_amarillo.pressed.connect(lambda: self.activar_tabulador(2))


        # Layout QStackedLayout
        # layout = QStackedLayout()
        # # Por default solo se visualiza el primer widget agregado
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('yellow'))
        # layout.setCurrentIndex(indice)

        # Layout Grid
        # layout = QGridLayout()
        # layout.addWidget(Color('red'),0,0)
        # layout.addWidget(Color('blue'), 0, 2)
        # layout.addWidget(Color('yellow'), 1, 0)
        # layout.addWidget(Color('green'), 1, 1)
        # layout.addWidget(Color('purple'), 1, 2)

        # # ** Layout vertical y horizontal
        # # layout = QVBoxLayout()
        # # layout = QHBoxLayout()
        # layout_horizontal = QHBoxLayout()
        # layout_vertical = QVBoxLayout()
        #
        # # Agregamos espacio al margel del layout horizontal
        # layout_horizontal.setContentsMargins(20,20,20,20)
        # # Agregamos espacios dentro de cada elemento del layout_horizontal
        # layout_horizontal.setSpacing(30)
        #
        # # Agregamos espacio en el layout vertical
        # layout_vertical.setContentsMargins(5,10,5,10)
        # # Agregamos espacios dentro de cada elemento del layout_vertical
        # layout_vertical.setSpacing(20)
        #
        # # Agregamos algunos widgets al layout_vertical
        # layout_vertical.addWidget(Color('red'))
        # layout_vertical.addWidget(Color('white'))
        # layout_vertical.addWidget(Color('blue'))
        # # Agregamos el layout_vertical dentro del layout_horizontal
        # layout_horizontal.addLayout(layout_vertical)
        # # Agregamos mas elementos al layout horizontal
        # layout_horizontal.addWidget(Color('yellow'))
        # layout_horizontal.addWidget(Color('purple'))
        # # Creamos un componente genérico para poder publicar el layout
        # componente = QWidget()
        # componente.setLayout(layout)
        # componente.setLayout(layout)

        self.setCentralWidget(tabulador)
        # color_fondo = Color('yellow')
        # El componente se expande para cubrir el tamaño disponible
        # self.setCentralWidget(color_fondo)

    def activar_tabulador(self, indice):
        self.layout_tipo_stack.setCurrentIndex(indice)
        print(f'Indice seleccionado: {indice}')



if __name__ == '__main__':
    app = QApplication()
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()