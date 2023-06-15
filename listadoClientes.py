import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QDesktopWidget, QVBoxLayout, QHBoxLayout, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QApplication, QToolBar, QAction, QMessageBox
from PyQt5 import QtGui

from cliente import Cliente

class ListadoClientes(QMainWindow):

    # metodo constructor de la ventana
    def __init__(self, clientes=None):
        super(ListadoClientes, self).__init__(clientes)

        # creamos un atributo que guarde la ventana anterior
        self.clientes = clientes

        # Titulo de la ventana
        self.setWindowTitle("Listado de Clientes")

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

        # abrimos el archivo en modo lectura
        self.file = open('archivos_planos/clientes.txt', 'rb')

        # lista vacia para guardar los usuarios
        usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # obtenemos del string una lista de 4 datos separados por ;
            lista = linea.split(";")

            # se para si ya no hay registros en el archivo
            if linea == '':
                break

            # creamos un objeto tipo cliente llamado u
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
            )

            # metemos el objeto en la lista usuario
            usuarios.append(u)

        # cerramos el archivo
        self.file.close()

        # Ya tenemos la lista con todos los usuarios

        # Obtenemos el numero de usuarios registrados:
        # Consultamos el tamano de la lista usuarios:
        self.numeroUsuarios = len(usuarios)

        # Contador de elementos para controlar a los usuarios en la tabla:
        self.contador = 0

        # Creamos un scroll:
        self.scrollArea = QScrollArea()

        # Hacemos Que el scroll se adapte a diferentes tamanos:
        self.scrollArea.setWidgetResizable(True)

        # Creamos una tabla:
        self.tabla = QTableWidget()
        self.tabla.setStyleSheet('background-color: #FFFFFF;')

        # definimos el numero de columnas que tendra la tabla:
        self.tabla.setColumnCount(4)

        # definimos el ancho de cada columna:
        self.tabla.setColumnWidth(0, 120)
        self.tabla.setColumnWidth(1, 190)
        self.tabla.setColumnWidth(2, 200)
        self.tabla.setColumnWidth(3, 150)

        # Definimos el texto de la cabecera:
        self.tabla.setHorizontalHeaderLabels(['Cedula',
                                              'Nombre',
                                              'Direccion',
                                              'Celular'])

        # Establecemos el numero de filas:
        self.tabla.setRowCount(self.numeroUsuarios)

        # Llenamos la tabla:
        for u in usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.cedula))
            # Hacemos que el nombre no se pueda editar:
            self.tabla.item(self.contador, 0).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.nombreCompleto))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.direccion))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.celular))
            # Hacemos que el documento no se pueda editar:
            #self.tabla.item(self.contador, 3).setFlags(Qt.ItemIsEnabled)
            self.contador += 1

        # Metemos la tabla en el scroll:
        self.scrollArea.setWidget(self.tabla)

        # Metemos en el layout vertical el scroll:
        self.verticalCentral.addWidget(self.scrollArea)

        # poner al ultimo
        # establecemos verticalCentral como layout del verticalcentral
        self.central.setLayout(self.verticalCentral)

    def accion_botonVolver(self):
        self.hide()
        self.clientes.show()

if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto del tipo realizarPedido con el nombre de RealizarPedido
    listadoClientes = ListadoClientes()

    # hacer que RealizarPedido se vea
    listadoClientes.show()

    # para cerrar la aplicacion
    sys.exit(app.exec_())