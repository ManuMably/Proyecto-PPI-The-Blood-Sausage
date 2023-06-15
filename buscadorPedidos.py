import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, \
    QLabel, QFormLayout, QLineEdit


class BuscadorPedidos(QMainWindow):

    def __init__(self, anterior=None):
        super(BuscadorPedidos, self).__init__(anterior)

        self.ventanaAnterior = anterior
        # generador de la ventana -----------------------------------
        # Titulo de la ventana
        self.setWindowTitle("Buscador De Pedidos")

        # ponemos color de fondo a la ventana
        self.setStyleSheet("background-color: #292828")

        # Ancho y alto de la ventana
        self.ancho = 700
        self.alto = 850

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
        #------------------------------------ fin generador de la ventana--------------------

        # ventana contenedora de todos los elementos
        self.centralBuscadorPedidos = QWidget()
        # establecemos la ventana contenedora como principal
        self.setCentralWidget(self.centralBuscadorPedidos)
        # definimos layout de la ventana centralInicioSesion
        self.verticalCentral = QVBoxLayout()
        self.verticalCentral.setAlignment(Qt.AlignCenter)



        # imagen logo--------------------------------------------------
        self.labelLogo = QLabel()
        self.logo = QPixmap('imagenes/logoSausage.png')
        self.labelLogo.setStyleSheet("margin-left: 50px;")
        self.labelLogo.setFixedHeight(200)
        self.labelLogo.setPixmap(self.logo)
        self.labelLogo.setAlignment(Qt.AlignHCenter)
        # agregamos la imagen al layout principal
        #self.layoutSalirLogo.addWidget(self.labelLogo)
        self.verticalCentral.addWidget(self.labelLogo)

        # ---------------creamos un layout para datos del pedido-------
        self.datosPedido = QWidget()
        self.formularioDatosPedido = QFormLayout()
        self.datosPedido.setLayout(self.formularioDatosPedido)



        # creamos el letrero Codigo de Pedido:
        self.codigoPedido = QLabel()
        # texto de letrero
        self.codigoPedido.setText("Codigo del Pedido:")
        # tipo de letra del letrero
        self.codigoPedido.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.codigoPedido.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                        "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                        "border-width: 1px; border-color: #000000;"
                                        "border-radius: 7px;margin-bottom: 5px;")
        self.codigoPedido.setAlignment(Qt.AlignCenter)
        self.codigoPedido.setFixedWidth(200)

        self.codigoPedidoN = QLabel()
        self.codigoPedidoN.setText("Aqui va el codigo de la tabla")
        self.codigoPedidoN.setFixedWidth(250)
        self.codigoPedidoN.setStyleSheet("background-color: #FFFFFF; margin-left: 20px;"
                                         "margin-right: 10px ;color: #61433f; border: solid;"
                                         "border-width: 1px; border-color: #000000;"
                                         "border-radius: 7px;margin-bottom: 10px;")

        self.formularioDatosPedido.addRow(self.codigoPedido, self.codigoPedidoN)

        # creamos el letrero nombre del cliente
        self.letreroCliente = QLabel()
        # texto de letrero
        self.letreroCliente.setText("Nombre:")
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
        self.nombreCliente = QLabel()
        self.nombreCliente.setText("Aqui va el nombre del cliente en el pedido")
        self.nombreCliente.setFixedWidth(250)
        self.nombreCliente.setStyleSheet("background-color: #FFFFFF; margin-left: 20px;"
                                         "margin-right: 10px ;color: #61433f; border: solid;"
                                         "border-width: 1px; border-color: #000000;"
                                         "border-radius: 7px;margin-bottom: 5px;")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioDatosPedido.addRow(self.letreroCliente, self.nombreCliente)

        # creamos el letrero telefono de la Direccion
        self.letreroDireccion = QLabel()
        # texto de letrero
        self.letreroDireccion.setText("Direccion:")
        # tipo de letra del letrero
        self.letreroDireccion.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroDireccion.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                          "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom:5px;")
        self.letreroDireccion.setAlignment(Qt.AlignCenter)
        self.letreroDireccion.setFixedWidth(200)

        # creamos el campo para el celular del cliente
        self.direccionCliente = QLineEdit()
        self.direccionCliente.setFixedWidth(250)
        self.direccionCliente.setStyleSheet("background-color: #FFFFFF; margin-left: 20px;"
                                          "margin-right: 10px ;color: #61433f; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom: 5px;")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioDatosPedido.addRow(self.letreroDireccion, self.direccionCliente)

        # hacemos el boton para limpiar
        self.botonlimpiar = QPushButton("Actualizar Pedido")

        # establecemos el ancho del boton
        self.botonlimpiar.setFixedWidth(300)
        self.botonlimpiar.setFixedHeight(50)

        # le ponemos los estilos
        self.botonlimpiar.setStyleSheet("background-color: #515670; margin-left: 20px;"
                                        "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                        "border-radius: 15px;margin-bottom:5px;")

        self.botonlimpiar.setFont(QFont("Arial", 15))

        # self.botonlimpiar.clicked.connect(self.accion_botonlimpiar)

        self.formularioDatosPedido.addRow(self.botonlimpiar)

        # ----------hacemos el boton para guardar la orden -------------------------------------
        self.botonGuardar = QPushButton("Eliminar Pedido")

        # establecemos el ancho del boton
        self.botonGuardar.setFixedWidth(300)
        self.botonGuardar.setFixedHeight(50)

        # le ponemos los estilos
        self.botonGuardar.setStyleSheet("background-color: #515670; margin-left: 20px;"
                                        "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                        "border-radius: 15px;margin-bottom:5px;")

        self.botonGuardar.setFont(QFont("Arial", 15))
        #self.botonGuardar.clicked.connect(self.accion_guardarPedido)
        self.formularioDatosPedido.addRow(self.botonGuardar)

        self.verticalCentral.addWidget(self.datosPedido)

        # -------------------------- fin formulario nombre, celular y reiniciar orden --------------------











        # ------------------------- poner al ultimo del constructor -------------------------
        # establecemos verticalCentral como layout del centralInicioSesion
        self.centralBuscadorPedidos.setLayout(self.verticalCentral)










if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto del tipo iniciar sesion con el nombre de inicioSesion
    buscadorPedidos = BuscadorPedidos()

    # hacer que inicioSesion se vea
    buscadorPedidos.show()

    # para cerrar la aplicacion
    sys.exit(app.exec_())