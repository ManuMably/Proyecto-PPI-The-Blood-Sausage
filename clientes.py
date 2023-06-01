import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QScrollArea, QTableWidget, QVBoxLayout, QLabel, QApplication, QHBoxLayout, \
    QStyle, QTableWidgetItem, QPushButton, QLineEdit, QFormLayout

from cliente import Cliente

class Clientes(QMainWindow):

    def __init__(self, menuPrincipal=None):
        super(Clientes, self).__init__(menuPrincipal)

        # creamos un atributo que guarde la ventatana anterior menuPrincipal
        self.menuPrincipal = menuPrincipal

        # Titulo de la ventana
        self.setWindowTitle("Clientes")

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

        # -------------------------------bloque de boton salir y logo---------------------------------------------------
        # widget para distribucion
        self.salirYLogo = QWidget()
        # layout para salirYLogo
        self.layoutSalirLogo = QHBoxLayout()
        self.salirYLogo.setLayout(self.layoutSalirLogo)

        # boton Volver
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 35px; margin-right: 350px; margin-bottom: 150px;")
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

        # ------------------------------- Bloque donde ira la tabla ----------------------------------------

        # Abrimos el archivo en modo de lectura:
        self.file = open('archivos_planos/clientes.txt', 'rb')

        # lista vacia para guardar los usuarios:
        self.usuarios = []

        # recorremos el archivo, linea por linea:
        while self.file:

            linea = self.file.readline().decode('UTF-8')

            # obtenemos del string una lista con 11 datos separados por;
            lista = linea.split(";")
            # Separa si ya no hay mas registros en el archivo
            if linea == '':
                break
            # Creamos un objeto tipo cliente llamado u
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
            )
            # Metemos el objeto en la lista de usuarios:
            self.usuarios.append(u)

        # Cerramos el archivo:
        self.file.close()

        # En este punto tenemos la lista usuarios con todos los usuarios

        # Obtenemos el numero de usuarios registrados:
        # Consultamos el tamano de la lista usuarios:
        self.numeroUsuarios = len(self.usuarios)

        # Contador de elementos para controlar a los usuarios en la tabla:
        self.contador = 0

        # Creamos un scroll:
        self.scrollArea = QScrollArea()

        # Hacemos Que el scroll se adapte a diferentes tamanos:
        self.scrollArea.setWidgetResizable(True)

        # Creamos una tabla:
        self.tabla = QTableWidget()

        # definimos el numero de columnas que tendra la tabla:
        self.tabla.setColumnCount(3)

        # definimos el ancho de cada columna:
        self.tabla.setColumnWidth(0, 410)
        self.tabla.setColumnWidth(1, 410)
        self.tabla.setColumnWidth(2, 250)

        # Definimos el texto de la cabecera:
        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Direccion',
                                              'Celular'])

        # Establecemos el numero de filas:
        self.tabla.setRowCount(self.numeroUsuarios)

        # Llenamos la tabla:
        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            # Hacemos que el nombre no se pueda editar:
            self.tabla.item(self.contador, 0).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.direccion))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.celular))
            self.contador += 1

        # Aplicar hoja de estilo a la tabla
        self.tabla.setStyleSheet("QTableWidget { background-color: white; }")

        # Metemos la tabla en el scroll:
        self.scrollArea.setWidget(self.tabla)

        # Metemos en el layout vertical el scroll:
        self.verticalCentral.addWidget(self.scrollArea)


        '''# imagen logo
        self.labeTablaEmpleados = QLabel()
        self.logo = QPixmap('imagenes/ejemploTabla.PNG')
        self.labeTablaEmpleados.setStyleSheet("")
        self.labeTablaEmpleados.setFixedHeight(200)
        self.labeTablaEmpleados.setPixmap(self.logo)
        self.labeTablaEmpleados.setAlignment(Qt.AlignHCenter)
        # agregamos la imagen al layout principal
        #self.layoutSalirLogo.addWidget(self.labelTablaEmpleados)
        self.verticalCentral.addWidget(self.labeTablaEmpleados)'''

        # ------------------------------Bloque de botones ---------------------------------------------------
        # widget para distribucion de botones registrar, cambiar, eliminar
        self.bloqueBotones = QWidget()
        # layout para bloqueBotones
        self.layoutBloqueBotones = QHBoxLayout()
        self.bloqueBotones.setLayout(self.layoutBloqueBotones)

        # boton registrar
        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setStyleSheet("border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 35px; margin-bottom: 150px;")
        self.botonRegistrar.setFont(QFont("Arial", 15))
        # lo agregamos
        self.layoutBloqueBotones.addWidget(self.botonRegistrar)

        # boton Cambiar
        self.botonCambiar = QPushButton("Cambiar")
        self.botonCambiar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 35px; margin-bottom: 150px;")
        self.botonCambiar.setFont(QFont("Arial", 15))
        # lo agregamos
        self.layoutBloqueBotones.addWidget(self.botonCambiar)

        # boton Eliminar
        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 35px; margin-bottom: 150px;")
        self.botonEliminar.setFont(QFont("Arial", 15))
        # lo agregamos
        self.layoutBloqueBotones.addWidget(self.botonEliminar)


        # agragamos el bloque de botones a la vertical central
        self.verticalCentral.addWidget(self.bloqueBotones)



        # poner al ultimo
        # establecemos verticalCentral como layout del centralInicioSesion
        self.central.setLayout(self.verticalCentral)

    def accion_botonVolver(self):
        self.hide()
        self.menuPrincipal.show()

if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto del tipo realizarPedido con el nombre de RealizarPedido
    clientes = Clientes()

    # hacer que RealizarPedido se vea
    clientes.show()

    # para cerrar la aplicacion
    sys.exit(app.exec_())