import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QLabel, QApplication, QHBoxLayout, \
    QStyle, QPushButton, QLineEdit, QFormLayout


class RealizarPedido(QMainWindow):

    def __init__(self, parent=None):
        super(RealizarPedido, self).__init__(parent)

        # Titulo de la ventana
        self.setWindowTitle("Realizar pedido")

        # para poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/iconos/realizarPedido.png'))

        # ponemos color de fondo a la ventana
        self.setStyleSheet("background-color: #292828")

        # Ancho y alto de la ventana
        self.ancho = 1100
        self.alto = 650

        # Asignamos el tamaño de ancho y alto a la ventana
        self.resize(self.ancho, self.alto)

        # centrar la ventana
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # para que la ventana no cambie de tamaño
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # ventana central
        self.central = QWidget()
        # establecemos la ventana central como principal
        self.setCentralWidget(self.central)
        # definimos layout de la ventana central
        self.verticalCentral = QVBoxLayout()

        # cramos un layout horizontal para el boton volver y el logo
        self.horizontalVolverLogo = QHBoxLayout()

        # boton volver
        self.iconoSalir = self.style().standardIcon(QStyle.SP_ArrowBack)
        self.botonVolver = QPushButton(self.iconoSalir, "Volver")
        self.botonVolver.setStyleSheet("border-radius: 15px; background-color: #515670;"
            "color: #FFFFFF; margin-left: 35px; margin-right: 200px; margin-bottom: 10px;")
        self.botonVolver.setFont(QFont("Arial", 15))
        self.botonVolver.setFixedWidth(400)
        self.botonVolver.clicked.connect(self.accion_botonVolver)
        self.horizontalVolverLogo.addWidget(self.botonVolver)

        self.horizontalVolverLogo.addStretch()

        # imagen logo
        self.labelLogo = QLabel()
        self.logo = QPixmap('imagenes/logoSausage.png')
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setFixedHeight(80)
        self.labelLogo.setFixedWidth(300)
        self.labelLogo.setPixmap(self.logo)
        self.labelLogo.setAlignment(Qt.AlignHCenter)
        self.horizontalVolverLogo.addWidget(self.labelLogo)

        self.verticalCentral.addLayout(self.horizontalVolverLogo)

        # creamos el letrero realizar pedido
        self.letreroRealizarPedido = QLabel()
        # texto de letreroInicioSesion
        self.letreroRealizarPedido.setText("Realizar Pedido")
        # tipo de letra del letrero
        self.letreroRealizarPedido.setFont(QFont("Arial", 25))
        # estilo del letreto
        self.letreroRealizarPedido.setStyleSheet("color: #FFFFFF;")
        self.letreroRealizarPedido.setFixedHeight(40)
        # centrar el texto
        self.letreroRealizarPedido.setAlignment(Qt.AlignCenter)

        self.verticalCentral.addWidget(self.letreroRealizarPedido)

        # creamos un layout para datos del cliente y pedido
        self.formularioDatosPedido = QFormLayout()

        # creamos el letrero nombre del cliente
        self.letreroCliente = QLabel()
        # texto de letrero
        self.letreroCliente.setText("Cliente")
        # tipo de letra del letrero
        self.letreroCliente.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroCliente.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                          "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom: 5px;")
        self.letreroCliente.setAlignment(Qt.AlignCenter)
        self.letreroCliente.setFixedWidth(200)

        # creamos el campo para el nombre del cliente
        self.nombreCliente = QLineEdit()
        self.nombreCliente.setFixedWidth(250)
        self.nombreCliente.setStyleSheet("background-color: #ffffff")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioDatosPedido.addRow(self.letreroCliente, self.nombreCliente)

        # creamos el letrero telefono del cliente
        self.letreroCelular = QLabel()
        # texto de letrero
        self.letreroCelular.setText("Celular")
        # tipo de letra del letrero
        self.letreroCelular.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroCelular.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                          "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom:5px;")
        self.letreroCelular.setAlignment(Qt.AlignCenter)
        self.letreroCelular.setFixedWidth(200)

        # creamos el campo para el celular del cliente
        self.celularCliente = QLineEdit()
        self.celularCliente.setFixedWidth(250)
        self.celularCliente.setStyleSheet("background-color: #ffffff")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioDatosPedido.addRow(self.letreroCelular, self.celularCliente)

        # agregamos el layout horozontal al layout principal
        self.verticalCentral.addLayout(self.formularioDatosPedido)
        self.verticalCentral.setSpacing(30)

        # hacemos el layout para las imagenes y letreros de precios
        self.horizontalProductos = QHBoxLayout()
        #self.horizontalProductos.setSpacing(30)


        self.producto1 = QVBoxLayout()

        # creamos un label para la imagen
        self.imagenMorcilla = QLabel()
        self.imagen1 = QPixmap('imagenes/morcilla.jpg')
        self.imagenMorcilla.setScaledContents(True)
        self.imagenMorcilla.setFixedWidth(150)
        self.imagenMorcilla.setFixedHeight(150)
        self.imagenMorcilla.setPixmap(self.imagen1)
        self.imagenMorcilla.setAlignment(Qt.AlignHCenter)
        self.producto1.addWidget(self.imagenMorcilla)
        #self.producto1.setAlignment(Qt.AlignCenter)

        #self.producto1.addStretch()

        # creamos el letrero para el precio
        self.precioMorcilla = QLabel()
        self.precioMorcilla.setText("15000")
        self.precioMorcilla.setFont(QFont("Arial", 10))
        self.precioMorcilla.setStyleSheet("background-color: #61433f; margin-left: 10px;"
                                          "margin-right: 50px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom:5px;")
        self.precioMorcilla.setAlignment(Qt.AlignCenter)
        self.precioMorcilla.setFixedWidth(200)
        self.precioMorcilla.setFixedHeight(50)
        self.producto1.addWidget(self.precioMorcilla)

        self.horizontalProductos.addLayout(self.producto1)

        self.horizontalBotones = QHBoxLayout()
        self.botonAgregar = QPushButton()
        self.botonAgregar.setText("+")
        self.botonAgregar.setStyleSheet("border-radius: 15px; background-color: #515670;"
                                        "color: #FFFFFF; margin-left: 10px; margin-right: 10px;"
                                        "margin-bottom: 10px;")
        self.botonAgregar.setFixedWidth(60)
        self.botonAgregar.setFixedHeight(60)
        self.horizontalBotones.addWidget(self.botonAgregar)

        self.botonDisminuir = QPushButton()
        self.botonDisminuir.setText("-")
        self.botonDisminuir.setStyleSheet("border-radius: 15px; background-color: #515670;"
                                          "color: #FFFFFF; margin-left: 10px; margin-right: 10px;"
                                          "margin-bottom: 10px;")
        self.botonDisminuir.setFixedWidth(60)
        self.botonDisminuir.setFixedHeight(60)
        self.horizontalBotones.addWidget(self.botonDisminuir)

        self.producto1.addLayout(self.horizontalBotones)
        self.horizontalProductos.addLayout(self.producto1)

        self.producto2 = QVBoxLayout()

        # creamos un label para la imagen
        self.imagenChorizo = QLabel()
        self.imagen2 = QPixmap('imagenes/chorizo.PNG')
        self.imagenChorizo.setScaledContents(True)
        self.imagenChorizo.setFixedWidth(150)
        self.imagenChorizo.setFixedHeight(150)
        self.imagenChorizo.setPixmap(self.imagen2)
        self.imagenChorizo.setAlignment(Qt.AlignHCenter)
        self.producto2.addWidget(self.imagenChorizo)

        # creamos el letrero para el precio
        self.precioChorizo = QLabel()
        self.precioChorizo.setText("18000")
        self.precioChorizo.setFont(QFont("Arial", 10))
        self.precioChorizo.setStyleSheet("background-color: #61433f; margin-left: 10px;"
                                         "margin-right: 50px ;color: #FFFFFF; border: solid;"
                                         "border-width: 1px; border-color: #000000;"
                                         "border-radius: 7px;margin-bottom:5px;")
        self.precioChorizo.setAlignment(Qt.AlignCenter)
        self.precioChorizo.setFixedWidth(200)
        self.precioChorizo.setFixedHeight(50)
        self.producto2.addWidget(self.precioChorizo)

        self.horizontalProductos.addLayout(self.producto2)

        self.horizontalBotones2 = QHBoxLayout()
        self.botonAgregar2 = QPushButton()
        self.botonAgregar2.setText("+")
        self.botonAgregar2.setStyleSheet("border-radius: 15px; background-color: #515670;"
                                         "color: #FFFFFF; margin-left: 10px; margin-right: 10px;"
                                         "margin-bottom: 10px;")
        self.botonAgregar2.setFixedWidth(60)
        self.botonAgregar2.setFixedHeight(60)
        self.horizontalBotones2.addWidget(self.botonAgregar2)

        self.botonDisminuir2 = QPushButton()
        self.botonDisminuir2.setText("-")
        self.botonDisminuir2.setStyleSheet("border-radius: 15px; background-color: #515670;"
                                           "color: #FFFFFF; margin-left: 10px; margin-right: 10px;"
                                           "margin-bottom: 10px;")
        self.botonDisminuir2.setFixedWidth(60)
        self.botonDisminuir2.setFixedHeight(60)
        self.horizontalBotones2.addWidget(self.botonDisminuir2)

        self.producto2.addLayout(self.horizontalBotones2)
        self.horizontalProductos.addLayout(self.producto2)

        self.producto3 = QVBoxLayout()

        # creamos un label para la imagen
        self.imagenArroz = QLabel()
        self.imagen3 = QPixmap('imagenes/arroz.jpg')
        self.imagenArroz.setScaledContents(True)
        self.imagenArroz.setFixedWidth(150)
        self.imagenArroz.setFixedHeight(150)
        self.imagenArroz.setPixmap(self.imagen3)
        self.imagenArroz.setAlignment(Qt.AlignHCenter)
        self.producto3.addWidget(self.imagenArroz)

        # creamos el letrero para el precio
        self.precioArroz = QLabel()
        self.precioArroz.setText("12000")
        self.precioArroz.setFont(QFont("Arial", 10))
        self.precioArroz.setStyleSheet("background-color: #61433f; margin-left: 10px;"
                                       "margin-right: 50px ;color: #FFFFFF; border: solid;"
                                       "border-width: 1px; border-color: #000000;"
                                       "border-radius: 7px;margin-bottom:5px;")
        self.precioArroz.setAlignment(Qt.AlignCenter)
        self.precioArroz.setFixedWidth(200)
        self.precioArroz.setFixedHeight(50)
        self.producto3.addWidget(self.precioArroz)

        self.horizontalProductos.addLayout(self.producto3)

        self.horizontalBotones3 = QHBoxLayout()
        self.botonAgregar3 = QPushButton()
        self.botonAgregar3.setText("+")
        self.botonAgregar3.setStyleSheet("border-radius: 15px; background-color: #515670;"
                                         "color: #FFFFFF; margin-left: 10px; margin-right: 10px;"
                                         "margin-bottom: 10px;")
        self.botonAgregar3.setFixedWidth(60)
        self.botonAgregar3.setFixedHeight(60)
        self.horizontalBotones3.addWidget(self.botonAgregar3)

        self.botonDisminuir3 = QPushButton()
        self.botonDisminuir3.setText("-")
        self.botonDisminuir3.setStyleSheet("border-radius: 15px; background-color: #515670;"
                                           "color: #FFFFFF; margin-left: 10px; margin-right: 10px;"
                                           "margin-bottom: 10px;")
        self.botonDisminuir3.setFixedWidth(60)
        self.botonDisminuir3.setFixedHeight(60)
        self.horizontalBotones3.addWidget(self.botonDisminuir3)

        self.producto3.addLayout(self.horizontalBotones3)
        self.horizontalProductos.addLayout(self.producto3)

        self.horizontalProductos.addStretch()

        self.verticalCentral.addLayout(self.horizontalProductos)





        # establecemos verticalCentral como layout del centralInicioSesion
        self.central.setLayout(self.verticalCentral)

    def accion_botonVolver(self):
        pass

if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto del tipo realizarPedido con el nombre de RealizarPedido
    realizarPedido = RealizarPedido()

    # hacer que RealizarPedido se vea
    realizarPedido.show()

    # para cerrar la aplicacion
    sys.exit(app.exec_())