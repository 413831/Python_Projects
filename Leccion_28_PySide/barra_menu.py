from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QMainWindow, QTabWidget, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Barra de herramientas')
        self.resize(600,400)
        etiqueta = QLabel('Hola')
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)

        # Creamos la barra de herramientas
        barra = QToolBar('Mi barra de herramientas')
        barra.setIconSize(QSize(16,16))
        # Configuración para mostrar la barra de herramientas
        # barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        # barra.setToolButtonStyle(Qt.ToolButtonTextOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonIconOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(barra)

        # Agregamos un elemento a nuestra barra de herramientas
        boton_nuevo = QAction(QIcon('nuevo.png'),'Nuevo',self)
        boton_guardar = QAction(QIcon('guardar.png'), 'Guardar', self)
        # Agregamos el boton a la barra
        barra.addAction(boton_nuevo)
        barra.addAction(boton_guardar)
        # Barra de estado
        self.setStatusBar(QStatusBar(self))
        # Mostramos mensaje del boton accion
        boton_nuevo.setStatusTip('Nuevo archivo')
        boton_guardar.setStatusTip('Guardar')

        # Asociamos el evento click
        boton_nuevo.triggered.connect(self.click_nuevo)
        boton_guardar.triggered.connect(self.click_guardar)

        barra.addSeparator()
        barra.addWidget(QCheckBox())
        barra.addWidget(QLabel('Salir'))

        menu = self.menuBar()
        menu_archivo = menu.addMenu('&Archivo')
        menu_archivo.addAction(boton_nuevo)
        # Agregamos una segunda opcion
        menu_archivo.addAction(boton_guardar)
        # Agregamos un separador
        menu_archivo.addSeparator()
        # Agregamos una tercera opcion
        boton_salir = QAction('Salir',self)
        menu_archivo.addAction(boton_salir)
        # Submenú ayuda
        boton_acerca_de = QAction(QIcon('acerca.png'), 'Acerca de',self)
        boton_acerca_de.triggered.connect(self.click_acerca_de)
        menu_ayuda = menu.addMenu('&Ayuda')
        menu_ayuda.addAction(boton_acerca_de)

        # Agregamos un submeno
        menu_archivo.addMenu(menu_ayuda)

        # Creación de atajos para nuestro menu
        # Ej. Combinación de teclas
        # boton_nuevo.setShortcut(QKeySequence('Ctrl+n'))
        boton_nuevo.setShortcut(Qt.CTRL + Qt.Key_N)
        # Atajos acerca de - Ctrl + 1
        boton_acerca_de.setShortcut(Qt.CTRL + Qt.Key_1)
        # Atajos guardar - Ctrl + S
        boton_guardar.setShortcut(Qt.CTRL + Qt.Key_S)


        # Hacemos chequeable el botón
        # boton_nuevo.setCheckable(True)

    def click_acerca_de(self, state):
        print(f'Acerca de...{state}')

    def click_nuevo(self, state):
        print(f'Nuevo archivo: {state}')

    def click_guardar(self, state):
        print(f'Guardar: {state}')


if __name__ == '__main__':
    app = QApplication()
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
