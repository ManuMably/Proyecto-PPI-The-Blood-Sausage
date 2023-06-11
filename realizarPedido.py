import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QLabel, QApplication, QHBoxLayout, \
    QStyle, QPushButton, QLineEdit, QFormLayout, QMessageBox


class RealizarPedido(QMainWindow):

    def __init__(self, menuPrincipal=None):
        super(RealizarPedido, self).__init__(menuPrincipal)

        # creamos un atributo que guarde la ventatana anterior menuPrincipal
        self.menuPrincipal = menuPrincipal

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

        # ---------------------------bloque de boton salir y logo
        # widget para distribucion
        self.salirYLogo = QWidget()
        # layout para salirYLogo
        self.layoutSalirLogo = QHBoxLayout()
        self.salirYLogo.setLayout(self.layoutSalirLogo)

        # boton Volver
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 300px; margin-bottom: 150px;")
        self.botonVolver.setFont(QFont("Arial", 15))
        # ponemos el boton volver a funcionar
        self.botonVolver.clicked.connect(self.accion_botonVolver)
        # lo agregamos
        self.layoutSalirLogo.addWidget(self.botonVolver)

        # imagen logo
        self.labelLogo = QLabel()
        self.logo = QPixmap('imagenes/logoSausage.png')
        self.labelLogo.setStyleSheet("margin-left: 50px;")
        self.labelLogo.setFixedHeight(200)
        self.labelLogo.setPixmap(self.logo)
        self.labelLogo.setAlignment(Qt.AlignHCenter)
        # agregamos la imagen al layout principal
        self.layoutSalirLogo.addWidget(self.labelLogo)
        self.verticalCentral.addWidget(self.salirYLogo)

        # ---------------- fin bloque salir y logo

        # ------------ bloque horizontal para datos de clientes,limpiar y datos de pedido --------------------------
        self.datosClientePedido = QWidget()
        self.layoutDatosClientePedido = QHBoxLayout()
        self.datosClientePedido.setLayout(self.layoutDatosClientePedido)

        # ---------------creamos un layout para datos del cliente y boton limpiar y guardar-------
        self.datosCliente = QWidget()
        self.formularioDatosPedido = QFormLayout()
        self.datosCliente.setLayout(self.formularioDatosPedido)

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

        # hacemos el boton para limpiar
        self.botonlimpiar = QPushButton("Reiniciar Orden")

        # establecemos el ancho del boton
        self.botonlimpiar.setFixedWidth(300)
        self.botonlimpiar.setFixedHeight(50)

        # le ponemos los estilos
        self.botonlimpiar.setStyleSheet("background-color: #515670; margin-left: 20px;"
                                       "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                       "border-radius: 15px;margin-bottom:5px;")

        self.botonlimpiar.setFont(QFont("Arial", 15))

        #self.botonlimpiar.clicked.connect(self.accion_botonlimpiar)

        self.formularioDatosPedido.addRow(self.botonlimpiar)

        # ----------hacemos el boton para guardar la orden -------------------------------------
        self.botonGuardar = QPushButton("Guardar Orden")

        # establecemos el ancho del boton
        self.botonGuardar.setFixedWidth(300)
        self.botonGuardar.setFixedHeight(50)

        # le ponemos los estilos
        self.botonGuardar.setStyleSheet("background-color: #515670; margin-left: 20px;"
                                        "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                        "border-radius: 15px;margin-bottom:5px;")

        self.botonGuardar.setFont(QFont("Arial", 15))
        self.formularioDatosPedido.addRow(self.botonGuardar)


        self.layoutDatosClientePedido.addWidget(self.datosCliente)


        # -------------------------- fin formulario nombre, celular y reiniciar orden --------------------



        # hacemos el layout para las imagenes y letreros de precios
        self.datosProductos = QWidget()
        self.datosProductos.setStyleSheet("background-color: #ffffff; border-radius: 10px;")
        self.horizontalProductos = QHBoxLayout()
        self.datosProductos.setLayout(self.horizontalProductos)

        self.producto1 = QVBoxLayout()

        # creamos un label para la imagen
        self.imagenMorcilla = QLabel()
        self.imagen1 = QPixmap('imagenes/morcilla.jpg')
        #self.imagenMorcilla.setStyleSheet("margin-left: 20px;")
        self.imagenMorcilla.setScaledContents(True)
        self.imagenMorcilla.setFixedWidth(150)
        self.imagenMorcilla.setFixedHeight(150)
        self.imagenMorcilla.setPixmap(self.imagen1)
        self.imagenMorcilla.setAlignment(Qt.AlignHCenter)
        self.producto1.addWidget(self.imagenMorcilla)
        # self.producto1.setAlignment(Qt.AlignCenter)

        # self.producto1.addStretch()

        # creamos el letrero para el precio
        self.nombreMorcilla = QLabel()
        self.nombreMorcilla.setText("Morcilla")
        self.nombreMorcilla.setFont(QFont("Arial", 15))
        self.nombreMorcilla.setStyleSheet("background-color: #61433f; margin-left: 5px;"
                                          "color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom:5px;")
        self.nombreMorcilla.setAlignment(Qt.AlignCenter)
        self.nombreMorcilla.setFixedWidth(150)
        self.nombreMorcilla.setFixedHeight(50)
        self.producto1.addWidget(self.nombreMorcilla)

        # contador de producto 1 ---------------------------------
        self.cantidadProducto1 = QLabel()
        self.cantidadProducto1.setText("0")
        self.cantidadProducto1.setFont(QFont("Arial", 15))
        self.cantidadProducto1.setStyleSheet("background-color: #ffffff; margin-left: 20px;"
                                             "margin-right: 10px ;color: #000000; border: solid;"
                                             "border-radius: 15px;margin-bottom:5px; margin-left: 70px;")

        self.producto1.addWidget(self.cantidadProducto1)
        # fin contador producto1 ----------------------------------

        self.horizontalProductos.addLayout(self.producto1)

        self.horizontalBotones = QHBoxLayout()
        self.botonAgregar = QPushButton()
        self.botonAgregar.setText("+")
        self.botonAgregar.setFont(QFont("Arial", 20))
        self.botonAgregar.setStyleSheet("border-radius: 15px; background-color: #515670;"
                                        "color: #FFFFFF; margin-left: 20px;"
                                        "margin-bottom: 10px;")
        self.botonAgregar.setFixedWidth(50)
        self.botonAgregar.setFixedHeight(50)
        self.botonAgregar.clicked.connect(self.accion_botonMasP1)
        self.horizontalBotones.addWidget(self.botonAgregar)

        self.botonDisminuir = QPushButton()
        self.botonDisminuir.setText("-")
        self.botonDisminuir.setFont(QFont("Arial", 20))
        self.botonDisminuir.setStyleSheet("border-radius: 15px; background-color: #515670;"
                                          "color: #FFFFFF; margin-left: 20px;"
                                          "margin-bottom: 10px;")
        self.botonDisminuir.setFixedWidth(50)
        self.botonDisminuir.setFixedHeight(50)
        self.botonDisminuir.clicked.connect(self.accion_botonMenosP1)
        self.horizontalBotones.addWidget(self.botonDisminuir)

        self.producto1.addLayout(self.horizontalBotones)
        self.horizontalProductos.addLayout(self.producto1)


        self.producto2 = QVBoxLayout()

        # creamos un label para la imagen
        self.imagenChorizo = QLabel()
        self.imagen2 = QPixmap('imagenes/chorizo.PNG')
        #self.imagenChorizo.setStyleSheet("margin-left: 20px;")
        self.imagenChorizo.setScaledContents(True)
        self.imagenChorizo.setFixedWidth(150)
        self.imagenChorizo.setFixedHeight(150)
        self.imagenChorizo.setPixmap(self.imagen2)
        self.imagenChorizo.setAlignment(Qt.AlignHCenter)
        self.producto2.addWidget(self.imagenChorizo)

        # creamos el letrero para el precio
        self.nombreChorizo = QLabel()
        self.nombreChorizo.setText("Chorizo")
        self.nombreChorizo.setFont(QFont("Arial", 15))
        self.nombreChorizo.setStyleSheet("background-color: #61433f; margin-left: 5px;"
                                         ";color: #FFFFFF; border: solid;"
                                         "border-width: 1px; border-color: #000000;"
                                         "border-radius: 7px;margin-bottom:5px;")
        self.nombreChorizo.setAlignment(Qt.AlignCenter)
        self.nombreChorizo.setFixedWidth(150)
        self.nombreChorizo.setFixedHeight(50)
        self.producto2.addWidget(self.nombreChorizo)

        # contador de producto 2 ---------------------------------
        self.cantidadProducto2 = QLabel()
        self.cantidadProducto2.setText("0")
        self.cantidadProducto2.setFont(QFont("Arial", 15))
        self.cantidadProducto2.setStyleSheet("background-color: #ffffff; margin-left: 20px;"
                                             "margin-right: 10px ;color: #000000; border: solid;"
                                             "border-radius: 15px;margin-bottom:5px; margin-left: 70px;")

        self.producto2.addWidget(self.cantidadProducto2)
        # fin contador producto2 ----------------------------------

        self.horizontalProductos.addLayout(self.producto2)

        self.horizontalBotones2 = QHBoxLayout()
        self.botonAgregar2 = QPushButton()
        self.botonAgregar2.setText("+")
        self.botonAgregar2.setFont(QFont("Arial", 20))
        self.botonAgregar2.setStyleSheet("border-radius: 15px; background-color: #515670;"
                                         "color: #FFFFFF;margin-left: 10px;"
                                         "margin-bottom: 10px;")
        self.botonAgregar2.setFixedWidth(47)
        self.botonAgregar2.setFixedHeight(47)
        self.botonAgregar2.clicked.connect(self.accion_botonMasP2)
        self.horizontalBotones2.addWidget(self.botonAgregar2)

        self.botonDisminuir2 = QPushButton()
        self.botonDisminuir2.setText("-")
        self.botonDisminuir2.setFont(QFont("Arial", 20))
        self.botonDisminuir2.setStyleSheet("border-radius: 15px; background-color: #515670;"
                                           "color: #FFFFFF; margin-left: 10px;"
                                           "margin-bottom: 10px;")
        self.botonDisminuir2.setFixedWidth(47)
        self.botonDisminuir2.setFixedHeight(47)
        self.botonDisminuir2.clicked.connect(self.accion_botonMenosP2)
        self.horizontalBotones2.addWidget(self.botonDisminuir2)

        self.producto2.addLayout(self.horizontalBotones2)
        self.horizontalProductos.addLayout(self.producto2)

        self.producto3 = QVBoxLayout()

        # creamos un label para la imagen
        self.imagenArroz = QLabel()
        self.imagen3 = QPixmap('imagenes/arroz.jpg')
        #self.imagenArroz.setStyleSheet("margin-left: 10px;")
        self.imagenArroz.setScaledContents(True)
        self.imagenArroz.setFixedWidth(150)
        self.imagenArroz.setFixedHeight(150)
        self.imagenArroz.setPixmap(self.imagen3)
        self.imagenArroz.setAlignment(Qt.AlignHCenter)
        self.producto3.addWidget(self.imagenArroz)

        # creamos el letrero para el precio
        self.nombreArroz = QLabel()
        self.nombreArroz.setText("Arroz de Cerdo")
        self.nombreArroz.setFont(QFont("Arial", 15))
        self.nombreArroz.setStyleSheet("background-color: #61433f; margin-left: 5px;"
                                       "color: #FFFFFF; border: solid;"
                                       "border-width: 1px; border-color: #000000;"
                                       "border-radius: 7px;margin-bottom:5px;")
        self.nombreArroz.setAlignment(Qt.AlignCenter)
        self.nombreArroz.setFixedWidth(150)
        self.nombreArroz.setFixedHeight(50)
        self.producto3.addWidget(self.nombreArroz)

        # contador de producto 3 ---------------------------------
        self.cantidadProducto3 = QLabel()
        self.cantidadProducto3.setText("0")
        self.cantidadProducto3.setFont(QFont("Arial", 15))
        self.cantidadProducto3.setStyleSheet("background-color: #ffffff; margin-left: 20px;"
                                             "margin-right: 10px ;color: #000000; border: solid;"
                                             "border-radius: 15px;margin-bottom:5px; margin-left: 70px;")

        self.producto3.addWidget(self.cantidadProducto3)
        # fin contador producto2 ----------------------------------

        self.horizontalProductos.addLayout(self.producto3)

        self.horizontalBotones3 = QHBoxLayout()
        self.botonAgregar3 = QPushButton()
        self.botonAgregar3.setText("+")
        self.botonAgregar3.setFont(QFont("Arial", 20))
        self.botonAgregar3.setStyleSheet("border-radius: 15px; background-color: #515670;"
                                         "color: #FFFFFF; margin-left: 20px;"
                                         "margin-bottom: 10px;")
        self.botonAgregar3.setFixedWidth(50)
        self.botonAgregar3.setFixedHeight(50)
        self.botonAgregar3.clicked.connect(self.accion_botonMasP3)
        self.horizontalBotones3.addWidget(self.botonAgregar3)

        self.botonDisminuir3 = QPushButton()
        self.botonDisminuir3.setText("-")
        self.botonDisminuir3.setFont(QFont("Arial", 20))
        self.botonDisminuir3.setStyleSheet("border-radius: 15px; background-color: #515670;"
                                           "color: #FFFFFF; margin-left: 20px;"
                                           "margin-bottom: 10px;")
        self.botonDisminuir3.setFixedWidth(50)
        self.botonDisminuir3.setFixedHeight(50)
        self.botonDisminuir3.clicked.connect(self.accion_botonMenosP3)
        self.horizontalBotones3.addWidget(self.botonDisminuir3)

        self.producto3.addLayout(self.horizontalBotones3)
        self.horizontalProductos.addLayout(self.producto3)

        #   |self.horizontalProductos.addStretch()

        self.layoutDatosClientePedido.addWidget(self.datosProductos)
        self.verticalCentral.addWidget(self.datosClientePedido)






        # establecemos verticalCentral como layout del centralInicioSesion
        self.central.setLayout(self.verticalCentral)

    def accion_botonVolver(self):
        self.hide()
        self.menuPrincipal.show()

    def accion_botonMasP1(self):
        cantidadActual = int(self.cantidadProducto1.text())
        aumentoCantidad = cantidadActual + 1
        self.cantidadProducto1.setText(str(aumentoCantidad))
    def accion_botonMenosP1(self):
        cantidadActual = int(self.cantidadProducto1.text())
        if cantidadActual <= 0:
            return QMessageBox.warning(self, 'Alerta', 'No se permite cantidades menores que 0')
        else:
            disminucionCantidad = cantidadActual - 1
            self.cantidadProducto1.setText(str(disminucionCantidad))

    def accion_botonMasP2(self):
        cantidadActual = int(self.cantidadProducto2.text())
        aumentoCantidad = cantidadActual + 1
        self.cantidadProducto2.setText(str(aumentoCantidad))
    def accion_botonMenosP2(self):
        cantidadActual = int(self.cantidadProducto2.text())
        if cantidadActual <= 0:
            return QMessageBox.warning(self, 'Alerta', 'No se permite cantidades menores que 0')
        else:
            disminucionCantidad = cantidadActual - 1
            self.cantidadProducto2.setText(str(disminucionCantidad))

    def accion_botonMasP3(self):
        cantidadActual = int(self.cantidadProducto3.text())
        aumentoCantidad = cantidadActual + 1
        self.cantidadProducto3.setText(str(aumentoCantidad))
    def accion_botonMenosP3(self):
        cantidadActual = int(self.cantidadProducto3.text())
        if cantidadActual <= 0:
            return QMessageBox.warning(self, 'Alerta', 'No se permite cantidades menores que 0')
        else:
            disminucionCantidad = cantidadActual - 1
            self.cantidadProducto3.setText(str(disminucionCantidad))


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto del tipo realizarPedido con el nombre de RealizarPedido
    realizarPedido = RealizarPedido()

    # hacer que RealizarPedido se vea
    realizarPedido.show()

    # para cerrar la aplicacion
    sys.exit(app.exec_())