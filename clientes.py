import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QScrollArea, QTableWidget, QVBoxLayout, QLabel, QApplication, QHBoxLayout, \
    QStyle, QTableWidgetItem, QPushButton, QLineEdit, QFormLayout, QToolBar, QAction, QMessageBox, QDialogButtonBox, QDialog

from cliente import Cliente
from gestionClientes import GestionClientes
from listadoClientes import ListadoClientes

class Clientes(QMainWindow):

    def __init__(self, menuPrincipal=None):
        super(Clientes, self).__init__(menuPrincipal)

        # creamos un atributo que guarde la ventatana anterior menuPrincipal
        self.menuPrincipal = menuPrincipal

        # Titulo de la ventana
        self.setWindowTitle("Clientes")

        # para poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/iconos/clientes.png'))

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

        # ventana central
        self.central = QWidget()
        # establecemos la ventana central como principal
        self.setCentralWidget(self.central)
        # ponemos color de fondo a la ventana
        self.central.setStyleSheet("background-color: #292828")
        # definimos layout de la ventana central
        self.verticalCentral = QVBoxLayout()

        # -------------------------------bloque de boton salir y logo---------------------------------------------------
        # widget para distribucion
        self.salirYLogo = QWidget()
        # layout para salirYLogo
        self.layoutSalirLogo = QHBoxLayout()
        self.salirYLogo.setLayout(self.layoutSalirLogo)

        # boton Volver
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 20px; margin-right: 50px; margin-bottom: 150px;")
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

        # ------------------------------- Bloque del formulario registro de clientes ----------------------------------------

        # creamos un layout para el registo de clientes
        self.formularioRegistro = QFormLayout()

        # creamos el letrero cedula del cliente
        self.letreroCedula = QLabel()
        # texto de letrero
        self.letreroCedula.setText("Cedula")
        # tipo de letra del letrero
        self.letreroCedula.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroCedula.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                          "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom: 5px;")
        self.letreroCedula.setAlignment(Qt.AlignCenter)
        self.letreroCedula.setFixedWidth(200)

        # creamos el campo para el nombre del cliente
        self.cedulaCliente = QLineEdit()
        self.cedulaCliente.setFixedWidth(400)
        self.cedulaCliente.setMaxLength(10)
        self.cedulaCliente.setStyleSheet("background-color: #ffffff")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioRegistro.addRow(self.letreroCedula, self.cedulaCliente)

        # creamos el letrero nombre del cliente
        self.letreroNombre = QLabel()
        # texto de letrero
        self.letreroNombre.setText("Nombre")
        # tipo de letra del letrero
        self.letreroNombre.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroNombre.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                          "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom: 5px;")
        self.letreroNombre.setAlignment(Qt.AlignCenter)
        self.letreroNombre.setFixedWidth(200)

        # creamos el campo para el nombre del cliente
        self.nombreCliente = QLineEdit()
        self.nombreCliente.setFixedWidth(400)
        self.nombreCliente.setStyleSheet("background-color: #ffffff")

        # agregamos el letrero al layout formularioRegistro
        self.formularioRegistro.addRow(self.letreroNombre, self.nombreCliente)

        # creamos el letrero nombre del cliente
        self.letreroDireccion = QLabel()
        # texto de letrero
        self.letreroDireccion.setText("Direccion")
        # tipo de letra del letrero
        self.letreroDireccion.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroDireccion.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                          "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom: 5px;")
        self.letreroDireccion.setAlignment(Qt.AlignCenter)
        self.letreroDireccion.setFixedWidth(200)

        # creamos el campo para el nombre del cliente
        self.direccionCliente = QLineEdit()
        self.direccionCliente.setFixedWidth(400)
        self.direccionCliente.setStyleSheet("background-color: #ffffff")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioRegistro.addRow(self.letreroDireccion, self.direccionCliente)

        # creamos el letrero nombre del cliente
        self.letreroCelular = QLabel()
        # texto de letrero
        self.letreroCelular.setText("Celular")
        # tipo de letra del letrero
        self.letreroCelular.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroCelular.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                          "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom: 5px; margin-bottom: 30px;")
        self.letreroCelular.setAlignment(Qt.AlignCenter)
        self.letreroCelular.setFixedWidth(200)

        # creamos el campo para el nombre del cliente
        self.celularCliente = QLineEdit()
        self.celularCliente.setFixedWidth(400)
        self.celularCliente.setMaxLength(10)
        self.celularCliente.setStyleSheet("background-color: #ffffff")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioRegistro.addRow(self.letreroCelular, self.celularCliente)

        # boton registrar
        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(160)
        self.botonRegistrar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 20px; margin-bottom: 30px;")
        self.botonRegistrar.setFont(QFont("Arial", 15))
        # ponemos el boton Agregar a funcionar
        self.botonRegistrar.clicked.connect(self.accion_Registrar)

        # boton limpiar
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(160)
        self.botonLimpiar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 20px; margin-bottom: 30px;")
        self.botonLimpiar.setFont(QFont("Arial", 15))
        # ponemos el boton actualizar a funcionar
        self.botonLimpiar.clicked.connect(self.accion_Limpiar)

        self.formularioRegistro.addRow(self.botonRegistrar, self.botonLimpiar)

        # hacemos un boton para gestion de clientes
        self.gestionarClientes = QPushButton("Gestionar\nClientes")
        self.gestionarClientes.setFixedWidth(200)
        self.gestionarClientes.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 20px; margin-bottom: 20px;")
        self.gestionarClientes.setFont(QFont("Arial", 15))
        self.gestionarClientes.clicked.connect(self.accion_gestionarClientes)

        # hacemos un boton para gestion de clientes
        self.listadoClientes = QPushButton("Listado de\nClientes")
        self.listadoClientes.setFixedWidth(200)
        self.listadoClientes.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 20px; margin-bottom: 20px;")
        self.listadoClientes.setFont(QFont("Arial", 15))
        self.listadoClientes.clicked.connect(self.accion_listadoClientes)

        self.formularioRegistro.addRow(self.gestionarClientes, self.listadoClientes)

        # agregamos el formulario al layout vertical
        self.verticalCentral.addLayout(self.formularioRegistro)

        # poner al ultimo
        # establecemos verticalCentral como layout del verticalcentral
        self.central.setLayout(self.verticalCentral)

        # -------------------CONSTRUCCION DE LA VENTANA EMERGENTE-----------------------

        # creamos ventana de dialogo
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # definimos el tamaño de la ventana
        self.ventanaDialogo.resize(300, 150)

        # cramos un boton para aceptar
        self.botonAceptar = QDialogButtonBox.Ok
        self.opcionesBotones = QDialogButtonBox(self.botonAceptar)
        self.opcionesBotones.accepted.connect(self.ventanaDialogo.accept)

        # establecemos el titulo de la ventana
        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        # configuramos la ventana para que sea modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # creamos un layout vertical
        self.vertical = QVBoxLayout()

        # cramos un label para mensajes
        self.mensaje = QLabel("")

        # le ponemos estilos al label
        self.mensaje.setStyleSheet("background-color: #61433f; color: #FFFFFF; padding: 10px;")

        # agregamos el label de mensajes
        self.vertical.addWidget(self.mensaje)

        # agregamos las opciones de los botones
        self.vertical.addWidget(self.opcionesBotones)

        # establecemos el layout vertical a la ventana
        self.ventanaDialogo.setLayout(self.vertical)

    def accion_botonVolver(self):
        self.hide()
        self.menuPrincipal.show()

    def accion_Registrar(self):

        # variable para controlar que los datos ingresados son correctos
        self.datosCorrectos = True

        # validamos que se ingresen todos los campos
        if ( self.cedulaCliente.text() == ''
            or self.nombreCliente.text() == ''
            or self.direccionCliente.text() == ''
            or self.celularCliente.text() == ''):

            self.datosCorrectos = False

            # escribimos texto explicativo
            self.mensaje.setText("Debe ingresar todos los campos")

            # hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()
            self.accion_botonVolver()

            self.cedulaCliente.setText('')
            self.nombreCliente.setText('')
            self.direccionCliente.setText('')
            self.celularCliente.setText('')

        if ( self.cedulaCliente.text() and not self.cedulaCliente.text().isnumeric()
            or self.celularCliente.text() and not self.celularCliente.text().isnumeric()):

            self.datosCorrectos = False

            # escribimos texto explicativo
            self.mensaje.setText("Los campos Cedula o Celular deben ser numericos"
                                 "\nintente nuevamente.")

            # hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()
            self.accion_botonVolver()

            self.cedulaCliente.setText('')
            self.celularCliente.setText('')

        # si los datos estan correctos
        if self.datosCorrectos:

            # abrimos el archivo en modo agregar escribiendo datos en binario
            self.file = open('archivos_planos/clientes.txt', 'ab')

            # trae el texto de los QlineEdit y los agrega contatenados
            self.file.write(bytes(self.cedulaCliente.text() + ";"
                                  + self.nombreCliente.text() + ";"
                                  + self.direccionCliente.text() + ";"
                                  + self.celularCliente.text() + "\n", encoding='UTF-8'))
            # para cerrar el archivo
            self.file.close()

            # escribimos un texto explicativo
            self.mensaje.setText("El cliente ha sido registrado correctamente")

            # hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()
            self.accion_botonVolver()

            self.cedulaCliente.setText('')
            self.nombreCliente.setText('')
            self.direccionCliente.setText('')
            self.celularCliente.setText('')

            # abrimos en modo lectura en formato de bytes
            self.file = open('archivos_planos/clientes.txt', 'rb')

            # recorre el archivo linea por linea
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':  # para cuando encuentra una linea vacia
                    break
            self.file.close()

    def accion_Limpiar(self):

        self.cedulaCliente.setText('')
        self.nombreCliente.setText('')
        self.direccionCliente.setText('')
        self.celularCliente.setText('')

    def accion_gestionarClientes(self):
        self.hide()
        self.gentionClientes = GestionClientes(self)
        self.gentionClientes.show()

    def accion_listadoClientes(self):
        self.hide()
        self.listadoClientes = ListadoClientes(self)
        self.listadoClientes.show()


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto del tipo realizarPedido con el nombre de RealizarPedido
    clientes = Clientes()

    # hacer que RealizarPedido se vea
    clientes.show()

    # para cerrar la aplicacion
    sys.exit(app.exec_())