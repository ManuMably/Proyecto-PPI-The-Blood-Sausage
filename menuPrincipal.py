import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QWidget, QVBoxLayout, QLabel, QFormLayout, \
    QLineEdit, QPushButton, QHBoxLayout, QStyle

from realizarPedido import RealizarPedido

class MenuPrincipal(QMainWindow):

    def __init__(self, parent=None):
        super(MenuPrincipal, self).__init__(parent)

        # Titulo de la ventana
        self.setWindowTitle("Menu Principal")

        # ponemos color de fondo a la ventana
        self.setStyleSheet("background-color: #292828")

        # Ancho y alto de la ventana
        self.ancho = 700
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
#-----------------------------------------------------------------------------------------------------------------------

        # ventana contenedora de todos los elementos
        self.centralInicioSesion = QWidget()
        # establecemos la ventana contenedora como principal
        self.setCentralWidget(self.centralInicioSesion)
        # definimos layout de la ventana centralInicioSesion
        self.verticalCentral = QVBoxLayout()

        # bloque de boton salir y logo
        # widget para distribucion
        self.salirYLogo = QWidget()
        # layout para salirYLogo
        self.layoutSalirLogo = QHBoxLayout()
        self.salirYLogo.setLayout(self.layoutSalirLogo)

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

        # boton salir
        self.iconoSalir = self.style().standardIcon(QStyle.SP_ArrowBack)
        self.botonSalir = QPushButton(self.iconoSalir, "Salir")
        self.botonSalir.setStyleSheet("border-radius: 15px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 35px; margin-bottom: 150px;")
        self.botonSalir.setFont(QFont("Arial", 25))
        self.layoutSalirLogo.addWidget(self.botonSalir)



        """# creamos el menu Principal
        self.letreroMenuPrincipal = QLabel()
        # texto de letreroInicioSesion
        self.letreroMenuPrincipal.setText("Menu Principal")
        # tipo de letra del letrero
        self.letreroMenuPrincipal.setFont(QFont("Arial", 25))
        # estilo del letreto
        self.letreroMenuPrincipal.setStyleSheet("color: black; background-color: #36c9c6; border-top: solid;"
                                                "margin-left: 50px; margin-right: 50px; border-radius: 45px; border-bottom: solid; border-width: 2px")
        self.letreroMenuPrincipal.setFixedHeight(100)
        #centrar el texto
        self.letreroMenuPrincipal.setAlignment(Qt.AlignCenter)
        # agregamos el letreroMenuPrincipal al layout principal
        self.verticalCentral.addWidget(self.letreroMenuPrincipal)"""
#-----------------------------------------------------------------------------------------------------------------------
        # imagen de productos y menu principal
        self.productosYMenu = QWidget()
        self.layoutProductosMenu = QHBoxLayout()
        self.productosYMenu.setLayout(self.layoutProductosMenu)

        # imagenes de nuestros mejores productos
        self.imagenProductos = QLabel()
        self.imagenP = QPixmap('imagenes/productosestrella.JPG')
        self.imagenProductos.setPixmap(self.imagenP)
        self.imagenProductos.resize(self.imagenP.width(), self.imagenP.height())
        self.imagenProductos.setScaledContents(True)
        self.imagenProductos.setFixedWidth(350)
        # agregamos la imagen a layoutProductosMenu
        self.layoutProductosMenu.addWidget(self.imagenProductos)


        # Menu Principal
        self.menuPrincipal = QLabel()
        self.menuPrincipal.setAlignment(Qt.AlignCenter)
        self.layoutMenuPrincipal = QFormLayout()

        # boton realizar pedido
        self.iconoPedido = self.style().standardIcon(QStyle.SP_FileDialogStart)
        self.botonRealizarPedido = QPushButton(self.iconoPedido, "Realizar Pedido")
        self.botonRealizarPedido.setStyleSheet("border-radius: 5px; background-color: #ed6a5a; margin-left: 30px; margin-right: 30px; margin-bottom: 10px;")
        self.botonRealizarPedido.setFont(QFont("Arial", 15))
        self.botonRealizarPedido.clicked.connect(self.accion_botonRealizarPedido)
        self.layoutMenuPrincipal.addRow(self.botonRealizarPedido)

        # boton HistorialPedidos
        self.iconoHistorial = self.style().standardIcon(QStyle.SP_FileDialogDetailedView)
        self.botonHistorialPedidos = QPushButton(self.iconoHistorial, "Historial Pedidos")
        self.botonHistorialPedidos.setStyleSheet("border-radius: 5px; background-color: #ed6a5a; margin-left: 30px; margin-right: 30px; margin-bottom: 10px;")
        self.botonHistorialPedidos.setFont(QFont("Arial", 15))
        self.layoutMenuPrincipal.addRow(self.botonHistorialPedidos)

        # boton Clientes
        self.iconoClientes = self.style().standardIcon(QStyle.SP_DirHomeIcon)
        self.botonClientes = QPushButton(self.iconoClientes, "Clientes")
        self.botonClientes.setStyleSheet("border-radius: 5px; background-color: #ed6a5a; margin-left: 30px; margin-right: 30px; margin-bottom: 10px;")
        self.botonClientes.setFont(QFont("Arial", 15))
        self.layoutMenuPrincipal.addRow(self.botonClientes)

        # boton Usuarios
        self.iconoUsuarios = self.style().standardIcon(QStyle.SP_DialogYesButton)
        self.botonUsuarios = QPushButton(self.iconoUsuarios, "Usuarios")
        self.botonUsuarios.setStyleSheet("border-radius: 5px; background-color: #ed6a5a; margin-left: 30px; margin-right: 30px; margin-bottom: 10px;")
        self.botonUsuarios.setFont(QFont("Arial", 15))
        self.layoutMenuPrincipal.addRow(self.botonUsuarios)


        # layot de menuPrincipal
        self.menuPrincipal.setLayout(self.layoutMenuPrincipal)
        # agregamos el menu a layoutProductosMenu
        self.layoutProductosMenu.addWidget(self.menuPrincipal)

        # agregamos el formulario al verticalCentral
        self.verticalCentral.addWidget(self.productosYMenu)






        # establecemos verticalCentral como layout del centralInicioSesion
        self.centralInicioSesion.setLayout(self.verticalCentral)

    def accion_botonRealizarPedido(self):
        self.hide()
        self.realizarPedido = RealizarPedido(self)
        self.realizarPedido.show()


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto del tipo iniciar sesion con el nombre de inicioSesion
    menuPrincipal = MenuPrincipal()

    # hacer que inicioSesion se vea
    menuPrincipal.show()

    # para cerrar la aplicacion
    sys.exit(app.exec_())