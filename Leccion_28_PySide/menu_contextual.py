from PySide6.QtGui import QAction, QIcon, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QMenu


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Contextual')
        # Mostramos y conectamos el menu contextual
        # Mostramos y conectamos el menu contextual
        self.show()
        # Nos conectamos a la señal de CustomContextRequested
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.mostrar_menu_contexto)

    def mostrar_menu_contexto(self, posicion):
        menu_contextual = QMenu(self)
        boton_nuevo = QAction(QIcon('nuevo.png'),'Nuevo', self)
        boton_guardar = QAction(QIcon('guardar.png'),'Guardar',self)
        boton_salir = QAction(QIcon('salir.png'),'Salir', self)
        # Conectamos con la opcion triggered
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)
        boton_salir.triggered.connect(self.click_boton_salir)

        menu_contextual.addAction(boton_nuevo)
        menu_contextual.addAction(boton_guardar)
        menu_contextual.addAction(boton_salir)
        # Recuperamos la posicion del cursos como posicion global de la ventana padre
        # Y ejecutamos el menu contextual
        # evento.globalPos() - posicion global del click
        # self.mapToGlobal() - posicion del menu a desplegar
        menu_contextual.exec(self.mapToGlobal(posicion))

    # Slots
    def click_boton_nuevo(self, state):
        print('Opcion Nuevo')

    def click_boton_guardar(self, state):
        print('Opcion Guardar')

    def click_boton_salir(self, state):
        print('Opcion Salir')

if __name__ == '__main__':
    app = QApplication()
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
