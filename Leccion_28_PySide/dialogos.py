from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, \
    QMessageBox


class VentanaDialogo(QDialog):
    def __init__(self,padre=None):
        super().__init__(padre)
        self.setWindowTitle('Ventana de Dialogo')
        # Agregamos un boton de aceptar y otro de cancelar
        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.botones_dialog = QDialogButtonBox(botones)
        self.botones_dialog.accepted.connect(self.accept)
        self.botones_dialog.rejected.connect(self.reject)

        # Creamos un layout para publicar los botones
        self.layout = QVBoxLayout()
        mensaje = QLabel('Presiona alguno de los botones')
        self.layout.addWidget(mensaje)
        self.layout.addWidget(self.botones_dialog)
        self.setLayout(self.layout)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Diálogos')
        self.resize(600,400)
        # Agregamos un botón
        boton = QPushButton('Mostrar diálogo')
        boton.clicked.connect(self.click_boton)

        # Publicamos el botón
        self.setCentralWidget(boton)

    def click_boton(self, state):
        print(f'Click sobre boton {state}')
        # Creamos diálogo
        # dialogo = QMessageBox.question(self,"Diálogo con Pregunta",'Ventana con pregunta')
        dialogo = QMessageBox.critical(self, 'Problema Crítico', 'Ventana con problema crítico',
                                       buttons=QMessageBox.Discard |
                                               QMessageBox.NoToAll |
                                               QMessageBox.Ignore,
                                       defaultButton=QMessageBox.Discard)

        if dialogo == QMessageBox.Discard:
            print('Regreso el valor de Discard')
        elif dialogo == QMessageBox.NoToAll:
            print('Regreso el valor de No to All')
        elif dialogo == QMessageBox.Ignore:
            print('Regreso el valor de Ignore')

        # dialogo = QMessageBox(self)
        # dialogo.setWindowTitle('Dialogo con Pregunta')
        # dialogo.setText('Ventana de Dialogo con Pregunta')
        # # Agregamos los botones de la respuesta a la pregunta
        # dialogo.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # # Agregamos un ícono a la ventana de diálogo
        # dialogo.setIcon(QMessageBox.Question)
        # valor_retornado = dialogo.exec()
        # # Imprimir el valor retornado
        # print(f'Valor retornado: {valor_retornado}')



        # ** Creamos el diálogo
        # dialogo = VentanaDialogo(self)
        # valor_retorno = dialogo.exec()
        # print(f'Valor retornado: {valor_retorno}')
        # if valor_retorno:
        #     print('Se presiono Ok')
        # else:
        #     print('Se presiono Cancel')


if __name__ == '__main__':
    app = QApplication()
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
