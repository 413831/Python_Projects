import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Clase base de Qt (PySide)
# Se encarga de procesar los eventos (event loop)
app = QApplication()
# Crear un objeto ventana
# Cualquier  componente puede ser una ventana en PySide
# ventana = QPushButton('Botón PySide')
# Cambiar el título
ventana = QMainWindow()
ventana.setWindowTitle('Hola Mundo con PySide')
# Modificamos el tamaño de la ventana
ventana.resize(600, 400)
# Mostrar ventana
ventana.show()
# Se ejecuta la aplicación
sys.exit(app.exec())