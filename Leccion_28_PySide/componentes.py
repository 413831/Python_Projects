from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox, QComboBox, QListWidget, QLineEdit, QSpinBox, \
    QDoubleSpinBox, QSlider, QDial


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # self.setFixedSize(500, 600)

        dial = QDial()
        dial.setRange(-5, 50)

        dial.valueChanged.connect(self.cambio_valor)
        dial.sliderMoved.connect(self.slider_cambio_posicion)
        dial.sliderPressed.connect(self.slider_presionado)
        dial.sliderReleased.connect(self.slider_liberado)

        self.setCentralWidget(dial)

        # # QSlider es para valores numericos enteros en un slider (deslizadora)
        # slider = QSlider(Qt.Horizontal)
        # slider.setMinimum(5)
        # slider.setMaximum(10)
        # slider.setRange(-5, 8)
        #
        # # Conectamos a las señales
        # slider.valueChanged.connect(self.cambio_valor)
        # slider.sliderMoved.connect(self.slider_cambio_posicion)
        # slider.sliderPressed.connect(self.slider_presionado)
        # slider.sliderReleased.connect(self.slider_liberado)
        #
        # # Publicamos este componentes
        # self.setCentralWidget(slider)

        # # QSpinBox - valores numericos
        # # numero = QSpinBox()
        # # QDoubleSpinBox - valores flotantes
        # numero = QDoubleSpinBox()
        #
        # # Establecer un valor mínimo y el valor maximo
        # numero.setMinimum(-5.5)
        # numero.setMaximum(10.7)
        # numero.setRange(-5.5,10.7)
        # # Establecemos prefijo y sufijo
        # numero.setPrefix('$ ')
        # numero.setSuffix(' c')
        # # Establecemos el salto (step)
        # numero.setSingleStep(1.5)
        # # Nos conectamos al evento de cambio de valor
        # # Envia el valor numérico
        # numero.valueChanged.connect(self.cambio_valor)
        # # Envía el valor en texto incluyendo prefijo y sufijo
        # numero.textChanged.connect(self.cambio_texto)
        #
        # self.setCentralWidget(numero)

        # # ** Componente QLineEdit
        # linea_texto = QLineEdit()
        # self.setCentralWidget(linea_texto)
        # # Establecemos el máximo de caracteres a capturar
        # linea_texto.setMaxLength(15)
        # # Placeholder
        # linea_texto.setPlaceholderText('Introduce tu nombre:')
        # # Solo lectura
        # linea_texto.setReadOnly(False)
        # # Evento enter, cambio seleccion texto, cambio texto
        # linea_texto.returnPressed.connect(self.enter_presionado)
        # linea_texto.selectionChanged.connect(self.cambio_seleccion)
        # linea_texto.textChanged.connect(self.cambio_texto)
        # # Validacion (mask)
        # linea_texto.setInputMask('00-0000-0000')

        # ** Componente QListWidget se parece al combobox
        # lista = QListWidget()
        # # Agregamos elementos
        # lista.addItem('Uno')
        # lista.addItems(['Dos','Tres'])
        # # Monitoreamos el cambio del elemento seleccionado, tanto el elemento con el texto
        # lista.currentItemChanged.connect(self.cambio_elemento)
        # lista.currentTextChanged.connect(self.cambio_texto)

        # Publicamos este componente
        # self.setCentralWidget(lista)

        # ** Creamos un nuevo combo box (drop down list) **
        # combobox = QComboBox()
        # # Agregamos elementos
        # combobox.addItem('Uno')
        # combobox.addItems(['Dos','Tres'])
        # # ** Monitoreamos el cambio de elemento seleccionado, tanto de índice como de texto **
        # combobox.currentIndexChanged.connect(self.cambio_indice)
        # combobox.currentTextChanged.connect(self.cambio_texto)
        # # Hacemos editable el combobox
        # combobox.setEditable(True)

        # ** Especificamos la política de inserción **
        # No permite agregar nuevos elementos
        # combobox.setInsertPolicy(QComboBox.NoInsert)
        # Agregar al inicio de nuestro combobox
        # combobox.setInsertPolicy(QComboBox.InsertAtTop)
        # Modifica el elemento actual
        # combobox.setInsertPolicy(QComboBox.InsertAtCurrent)
        # Insertar al final
        # combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        # Insertar antes del elemento actual
        # combobox.setInsertPolicy(QComboBox.InsertBeforeCurrent)
        # Insertar despues del elemento actual
        # combobox.setInsertPolicy(QComboBox.InsertAfterCurrent)
        # Insertar alfabeticamente
        # combobox.setInsertPolicy(QComboBox.InsertAlphabetically)

        # Limitamos cuantos elementos agregamos al combobox
        # combobox.setMaxCount(6)

        # Publicamos este componente
        # self.setCentralWidget(combobox)


        # ** Creamos un nuevo checkbox **
        # checkbox = QCheckBox('Este es un checkbox')
        # # Activamos el tercer estado
        # # Tenemos 3 estados (0-Apagado, 1-Sin estado, 2-Seleccionado)
        # checkbox.setTristate(True)
        #
        # # Conectar la señal de cambio de componente
        # checkbox.stateChanged.connect(self.mostrar_estado)
        # # Publicamos este componentes
        # self.setCentralWidget(checkbox)


        # ** Creamos un componente de tipo etiqueta (Label) **
        # etiqueta = QLabel('Hola')
        # etiqueta.setPixmap(QPixmap('layla.jpg'))
        # etiqueta.setScaledContents(True)

        # Modificamos el valor inicial
        # etiqueta.setText('Saludos')
        # Modificamos la fuente
        # fuente = etiqueta.font()
        # fuente.setPointSize(25)
        # etiqueta.setFont(fuente)
        # # Modificar la alineación de la etiqueta
        # # etiqueta.setAlignment(Qt.AlignCenter)
        # etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Publicamos este componente
        # self.setCentralWidget(etiqueta)

    # Slots
    def cambio_valor(self, nuevo_valor):
        print(f'Nuevo valor: {nuevo_valor}')

    def slider_cambio_posicion(self, nueva_posicion):
        print(f'Nueva posicion: {nueva_posicion}')

    def slider_presionado(self):
        print('Presionado')

    def slider_liberado(self):
        print('Liberado')

    def cambio_seleccion(self):
        print('Cambio selección de texto')
        print(self.centralWidget().selectedText())


    def enter_presionado(self):
        print('Se presionó el enter')
        self.centralWidget().setText('00-0000-0000')


    def mostrar_estado(self, estado):
        print('Estado checkbox:',estado)
        # Trabajamos con las constantes
        if estado == Qt.Checked:
            print('Checkbox encendido')
        elif estado == Qt.PartiallyChecked:
            print('Checkbox sin estado o parcialmente seleccionado')
        elif estado == Qt.Unchecked:
            print('Checkbox apagado')
        else:
            print('Checkbox con estado inválido')


    def cambio_elemento(self, nuevo_elemento):
        print(f'Nuevo elemento seleccionado: {nuevo_elemento.text()}')

    def cambio_indice(self, nuevo_indice):
        print(f'Nuevo índice seleccionado: {nuevo_indice}')

    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto: {nuevo_texto}')


if __name__ == '__main__':
    app = QApplication()
    ventana = Componentes()
    ventana.show()
    app.exec()