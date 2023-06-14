import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, \
    QWidget, QFormLayout, QLineEdit, QScrollArea, QTableWidget, QTableWidgetItem

from pedido import Pedido


class VentanaHistorialPedidos(QMainWindow):

    def __init__(self, anterior=None):
        super(VentanaHistorialPedidos, self).__init__(anterior)

        self.ventanaAnterior = anterior

        # titulo de la ventana
        self.setWindowTitle("Historial Pedidos")

        # ancho y alto de la ventana
        self.ancho = 1100
        self.alto = 650

        # asignamos el tamano de ancho y alto a la ventana
        self.resize(self.ancho, self.alto)

        # centrar la ventana
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # para que la ventana no cambie de tamano
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        self.fondo.setStyleSheet("background-color: #292828")

        # establecemos la ventana fondo como ventana central
        self.setCentralWidget(self.fondo)

        # layout de fondo vertical
        self.verticalPrincipal = QVBoxLayout()

        self.verticalPrincipal.setSpacing(0)

        # ------------------------------------------------------------------------------
        # bloque boton volver y logo

        # widget que almacena el boton volver y el titulo
        self.volverYTitulo = QWidget()
        self.volverYTitulo.setFixedHeight(100)
        # definimos el layout del widget volverYTitulo
        self.horizontalVolverTitulo = QHBoxLayout()
        # asignamos el layout de volverYTitulo
        self.volverYTitulo.setLayout(self.horizontalVolverTitulo)

        # boton volver
        self.botonVolver = QPushButton("Volver")
        # estilo boton volver
        self.botonVolver.setStyleSheet("border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 35px; margin-right: 600px;")
        self.botonVolver.setFont(QFont("Arial", 15))
        # ponemos el boton volver a funcionar
        self.botonVolver.clicked.connect(self.accion_botonVolver)

        # agregamos al widget el boton volver
        self.horizontalVolverTitulo.addWidget(self.botonVolver)

        # imagen logo
        self.labelLogo = QLabel()
        self.logo = QPixmap('imagenes/logoSausage.png')
        self.labelLogo.setStyleSheet("margin-right: 50px;")
        self.labelLogo.setFixedWidth(300)
        # establecemos que se pueda escalar la imagen
        self.labelLogo.setScaledContents(True)
        # el tamaño de la imagen se adapta a la ventana
        self.resize(self.labelLogo.width(), self.labelLogo.height())
        self.labelLogo.setPixmap(self.logo)
        self.labelLogo.setAlignment(Qt.AlignHCenter)
        # agregamos la imagen al layout principal
        self.horizontalVolverTitulo.addWidget(self.labelLogo)
        #self.verticalCentral.addWidget(self.salirYLogo)

        # margen de la vertical principal
        self.verticalPrincipal.setContentsMargins(0, 0, 0, 0)
        self.verticalPrincipal.setSpacing(0)
        # agregamos el widget de volverYTitulo
        self.verticalPrincipal.addWidget(self.volverYTitulo)

        # ------------------------------- Bloque donde ira la tabla ----------------------------------------

        # Abrimos el archivo en modo de lectura:
        self.file = open('archivos_planos/pedidos.txt', 'rb')

        # lista vacia para guardar los usuarios:
        self.pedidos = []

        # recorremos el archivo, linea por linea:
        while self.file:

            linea = self.file.readline().decode('UTF-8')

            # obtenemos del string una lista con 11 datos separados por;
            lista = linea.split(";")
            # Separa si ya no hay mas registros en el archivo
            if linea == '':
                break
            # Creamos un objeto tipo cliente llamado u
            p = Pedido(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6]
            )
            # Metemos el objeto en la lista de usuarios:
            self.pedidos.append(p)

        # Cerramos el archivo:
        self.file.close()

        # En este punto tenemos la lista usuarios con todos los pedidos

        # Obtenemos el numero de usuarios registrados:
        # Consultamos el tamano de la lista usuarios:
        self.numeroPedidos = len(self.pedidos)

        # Contador de elementos para controlar a los usuarios en la tabla:
        self.contador = 0

        # Creamos un scroll:
        self.scrollArea = QScrollArea()


        # Hacemos Que el scroll se adapte a diferentes tamanos:
        self.scrollArea.setWidgetResizable(True)

        # Creamos una tabla:
        self.tabla = QTableWidget()

        # definimos el numero de columnas que tendra la tabla:
        self.tabla.setColumnCount(7)

        # definimos el ancho de cada columna:
        self.tabla.setColumnWidth(0, 250)
        self.tabla.setColumnWidth(1, 250)
        self.tabla.setColumnWidth(2, 250)
        self.tabla.setColumnWidth(3, 250)
        self.tabla.setColumnWidth(4, 250)
        self.tabla.setColumnWidth(5, 250)
        self.tabla.setColumnWidth(6, 250)

        # Definimos el texto de la cabecera:
        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Direccion',
                                              'Celular',
                                              'Cantidad Morcilla',
                                              'Cantidad Chorizo',
                                              'Cantidad Arroz',
                                              'Estado del Pedido'])

        # Establecemos el numero de filas:
        self.tabla.setRowCount(self.numeroPedidos)

        # Llenamos la tabla:
        for p in self.pedidos:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(p.nombreCliente))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(p.direccion))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(p.celular))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(p.morcillaCantidad))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(p.chorizoCantidad))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(p.arrozCantidad))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(p.estadoPedido))
            self.contador += 1

        # Aplicar hoja de estilo a la tabla
        self.tabla.setStyleSheet("QTableWidget { background-color: white; }")

        # Metemos la tabla en el scroll:
        self.scrollArea.setWidget(self.tabla)

        # Metemos en el layout vertical el scroll:
        self.verticalPrincipal.addWidget(self.scrollArea)

        # ------------------------------Bloque de botones ---------------------------------------------------
        # widget para distribucion de botones registrar, cambiar, eliminar
        self.bloqueBotones = QWidget()
        # layout para bloqueBotones
        self.layoutBloqueBotones = QHBoxLayout()
        self.bloqueBotones.setLayout(self.layoutBloqueBotones)

        # boton registrar
        self.botonRegistrar = QPushButton("Agregar")
        self.botonRegistrar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 35px; margin-bottom: 150px;")
        self.botonRegistrar.setFont(QFont("Arial", 15))
        # ponemos el boton Agregar a funcionar
        #self.botonRegistrar.clicked.connect(self.accion_add)
        # lo agregamos
        self.layoutBloqueBotones.addWidget(self.botonRegistrar)

        # boton Cambiar
        self.botonCambiar = QPushButton("Actualizar")
        self.botonCambiar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 35px; margin-bottom: 150px;")
        self.botonCambiar.setFont(QFont("Arial", 15))
        # ponemos el boton actualizar a funcionar
        #self.botonCambiar.clicked.connect(self.accion_insert)
        # lo agregamos
        self.layoutBloqueBotones.addWidget(self.botonCambiar)

        # boton Eliminar
        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 35px; margin-bottom: 150px;")
        self.botonEliminar.setFont(QFont("Arial", 15))
        # ponemos el boton Eliminar a funcionar
        #self.botonEliminar.clicked.connect(self.accion_delete)
        # lo agregamos
        self.layoutBloqueBotones.addWidget(self.botonEliminar)

        # agragamos el bloque de botones a la vertical central
        self.verticalPrincipal.addWidget(self.bloqueBotones)



        # establecemos el verticalPrincipal como layout de la ventana
        self.fondo.setLayout(self.verticalPrincipal)

    def accion_botonVolver(self):
            self.hide()
            self.ventanaAnterior.show()


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo ventana 1 con el nombre de ventana 1
    ventana = VentanaHistorialPedidos()

    # hacer que el objeto ventana 1 se vea
    ventana.show()

    # para terminar la aplicacion
    sys.exit(app.exec_())