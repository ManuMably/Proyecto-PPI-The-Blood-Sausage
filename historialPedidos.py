import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, \
    QWidget, QFormLayout, QLineEdit, QScrollArea, QTableWidget, QTableWidgetItem, QMessageBox

from buscadorPedidos import BuscadorPedidos
from pedido import Pedido


class VentanaHistorialPedidos(QMainWindow):

    def __init__(self, anterior=None):
        super(VentanaHistorialPedidos, self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.pedidoBusqueda = ""

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

            # obtenemos del string una lista con 9 datos separados por;
            lista = linea.split(";")
            # Separa si ya no hay mas registros en el archivo
            if linea == '':
                break
            # Creamos un objeto tipo Pedido llamado p
            p = Pedido(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8]
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
        self.tabla.setColumnCount(9)

        # definimos el ancho de cada columna:
        self.tabla.setColumnWidth(0, 100)
        self.tabla.setColumnWidth(1, 230)
        self.tabla.setColumnWidth(2, 230)
        self.tabla.setColumnWidth(3, 230)
        self.tabla.setColumnWidth(4, 230)
        self.tabla.setColumnWidth(5, 230)
        self.tabla.setColumnWidth(6, 230)
        self.tabla.setColumnWidth(7, 230)
        self.tabla.setColumnWidth(8, 230)

        # Definimos el texto de la cabecera:
        self.tabla.setHorizontalHeaderLabels(['Codigo Pedido', 'Nombre', 'Cedula',
                                              'Direccion',
                                              'Celular',
                                              'Cantidad Morcilla',
                                              'Cantidad Chorizo',
                                              'Cantidad Arroz',
                                              'Estado del Pedido',])

        # Establecemos el numero de filas:
        self.tabla.setRowCount(self.numeroPedidos)

        # Llenamos la tabla:
        for p in self.pedidos:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(p.codigoPedido))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(p.nombreCliente))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(p.cedulaCliente))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(p.direccion))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(p.celular))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(p.morcillaCantidad))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(p.chorizoCantidad))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(p.arrozCantidad))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(p.estadoPedido))
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

        # boton Cambiar
        self.botonCambiar = QPushButton("Actualizar")
        self.botonCambiar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 35px; margin-bottom: 20px;")
        self.botonCambiar.setFont(QFont("Arial", 15))
        # ponemos el boton actualizar a funcionar
        self.botonCambiar.clicked.connect(self.accion_insert)
        # lo agregamos
        self.layoutBloqueBotones.addWidget(self.botonCambiar)

        # boton Eliminar
        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 35px; margin-bottom: 20px;")
        self.botonEliminar.setFont(QFont("Arial", 15))
        # ponemos el boton Eliminar a funcionar
        self.botonEliminar.clicked.connect(self.accion_delete)
        # lo agregamos
        self.layoutBloqueBotones.addWidget(self.botonEliminar)

        # boton Refrescar
        self.botonRefrescar = QPushButton("Refrescar")
        self.botonRefrescar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 35px; margin-bottom: 20px;")
        self.botonRefrescar.setFont(QFont("Arial", 15))
        # ponemos el boton Eliminar a funcionar
        self.botonRefrescar.clicked.connect(self.accion_botonRefrescar)
        # lo agregamos
        self.layoutBloqueBotones.addWidget(self.botonRefrescar)

        # agragamos el bloque de botones a la vertical central
        self.verticalPrincipal.addWidget(self.bloqueBotones)

        # bloque del buscador ----------------------------------------------
        # creamos el letrero codigo Pedido
        self.letreroCodigoPedido = QLabel()
        # texto de letrero
        self.letreroCodigoPedido.setText("Ingresa el codigo del pedido que desees buscar:")
        # tipo de letra del letrero
        self.letreroCodigoPedido.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroCodigoPedido.setStyleSheet("background-color: #61433f; margin-left: 300px; margin-right: 300px ;"
                                          "color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom:5px;")
        self.letreroCodigoPedido.setAlignment(Qt.AlignCenter)
        #self.letreroCodigoPedido.setFixedWidth(200)

        self.verticalPrincipal.addWidget(self.letreroCodigoPedido)

        # creamos el campo para el ingreso del codigo a buscar
        self.ingresoCodigoBuscador = QLineEdit()
        #self.ingresoCodigoBuscador.setFixedWidth(250)
        self.ingresoCodigoBuscador.setStyleSheet("background-color: #FFFFFF; margin-left: 500px;"
                                          "margin-right: 500px ; color: #61433f; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom: 15px;")
        self.ingresoCodigoBuscador.setAlignment(Qt.AlignHCenter)
        self.verticalPrincipal.addWidget(self.ingresoCodigoBuscador)

        # boton buscar
        self.botonBuscar = QPushButton("Buscar")
        self.botonBuscar.setStyleSheet("border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 400px; margin-right: 400px; margin-bottom: 20px;")
        self.botonBuscar.setFont(QFont("Arial", 15))
        # ponemos el boton buscar a funcionar
        self.botonBuscar.clicked.connect(self.accion_botonBuscar)
        # lo agregamos
        self.verticalPrincipal.addWidget(self.botonBuscar)






        # establecemos el verticalPrincipal como layout de la ventana
        self.fondo.setLayout(self.verticalPrincipal)

    def accion_botonRefrescar(self):
        self.fondo.update()
        print("post")
    def accion_botonBuscar(self):
        print("presionado")
        # Abrimos el archivo en modo de lectura:
        self.file = open('archivos_planos/pedidos.txt', 'rb')

        # lista vacia para guardar los usuarios:
        self.pedidos2 = []

        # recorremos el archivo, linea por linea:
        while self.file:

            linea = self.file.readline().decode('UTF-8')

            # obtenemos del string una lista con 9 datos separados por;
            lista = linea.split(";")
            # Separa si ya no hay mas registros en el archivo
            if linea == '':
                break
            # Creamos un objeto tipo Pedido llamado p
            p = Pedido(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8]
            )
            # Metemos el objeto en la lista de usuarios:
            self.pedidos2.append(p)

        # Cerramos el archivo:
        self.file.close()

        # En este punto tenemos la lista pedidos con todos los pedidos

        #bandera para controlar si no se encontro el pedido
        self.banderaPedidoBusqueda = False

        # Recorremos la lista de pedidos

        for p in self.pedidos2:
            # buscamos el usuario por el nombre:
            if (p.codigoPedido == self.ingresoCodigoBuscador.text()):
                self.pedidoBusqueda = self.ingresoCodigoBuscador.text()
                print(self.pedidoBusqueda)
                self.banderaPedidoBusqueda = True
                self.ingresoCodigoBuscador.setText("")

                self.hide()
                self.buscadorPedidos = BuscadorPedidos(self)
                self.buscadorPedidos.show()

                # paramos el for:
                break
        if not self.banderaPedidoBusqueda:
            return QMessageBox.warning(self, 'Alerta', 'no se encontro el codigo de pedido')






    def accion_botonVolver(self):
            self.hide()
            self.ventanaAnterior.show()

    def accion_delete(self):

        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self,
                                       'Alerta',
                                       'Para borrar, se debe seleccionar un registro')

        boton = QMessageBox.question(self,
                                    'Confirmacion',
                                    '¿Esta seguro de que quieres borrar este registro?',
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                                )

        if boton == QMessageBox.StandardButton.Yes:

            if (
                self.tabla.item(filaActual, 0).text() != '' and
                self.tabla.item(filaActual, 1).text() != '' and
                self.tabla.item(filaActual, 2).text() != ''
            ):

                # Abrimos el archivo en modo de lectura:
                self.file = open('archivos_planos/pedidos.txt', 'rb')

                # lista vacia para guardar los usuarios:
                pedidos = []

                # Iteramos sobre el archivo linea por linea:
                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    # obtenemos dle string una lista con 11 datos separados por ;
                    lista = linea.split(";")
                    # va a parar si ya no hay mas registros en el archivo
                    if linea == '':
                        break
                    # creamos un objeto tipo cliente llamado u
                    # y le pasamos los elementos de la lista:
                    p = Pedido(
                        lista[0],
                        lista[1],
                        lista[2],
                        lista[3],
                        lista[4],
                        lista[5],
                        lista[6],
                        lista[7],
                        lista[8]
                    )
                    # metemos el objeto en la lista de usuarios:
                    pedidos.append(p)

                # cerramos el archivo:
                self.file.close()

                # en este punto tenemos la lista usuarios con todos los usuarios:

                # Recorremos la lista de usuarios
                for p in pedidos:
                    # buscamos el usuario por el nombre:
                    if (
                            p.codigoPedido == self.tabla.item(filaActual, 0).text()
                    ):

                        # Removemos el usuario de la lista de usuarios:
                        pedidos.remove(p)

                        # paramos el for:
                        break

                # Abrimos el archivo en modo escritura para reescribir los datos sin el usuario borrado.
                self.file = open('archivos_planos/clientes.txt', 'wb')

                # recorremos la lista de usuarios
                # para guardar usuario por usuario en el archivo
                for p in pedidos:
                    self.file.write(bytes(p.codigoPedido + ";" + p.cedulaCliente.strip() + ";" + p.nombreCliente + ";" + p.direccion.strip() + ";" + p.celular.strip() + ";" + p.morcillaCantidad.strip() + ";" + p.chorizoCantidad.strip() + ";" + p.arrozCantidad.strip() + ";" + p.estadoPedido.strip() + "\n", encoding='UTF-8'))
                self.file.close()

                # Hacemos que en la tabla no se vea el registro:
                self.tabla.removeRow(filaActual)

                return QMessageBox.question(self,
                                            'Confirmation',
                                            'El registro ha sido eliminado exitosamente.',
                                            QMessageBox.StandardButton.Yes
                                        )
            else:
                # Hacemos que en la tabla no se vea el registro en case de tratarse de una fila vacia:
                self.tabla.removeRow(filaActual)

    def accion_insert(self):

        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self, 'Alerta', 'Para Modificar, debe seleccionar un registro')

        boton = QMessageBox.question(self,
                                    'Confirmacion',
                                    '¿Esta seguro de que quiere modificar este registro?',
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                                )

        # variable para controlar que se hayan ingresado todos los datos:
        datosVacios = True

        if boton == QMessageBox.StandardButton.Yes:

            # Validamos que se hayan ingresado los datos:
            if (
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != ''
            ):
                # Actualizamos la variable para indicar que se ingresaron todos los datos:
                datosVacios = False

                # Abrimos el archivo en modo de lectura:
                self.file = open('archivos_planos/pedidos.txt', 'rb')

                # lista vacia para guardar los usuarios:
                pedidos = []

                # Iteramos sobre el archivo liena por linea:
                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    # obtenemos del string una lista con 11 datos separados por ;
                    lista = linea.split(";")
                    # se detiene si yan o hay mas Registros en el archivo
                    if linea == '':
                        break
                    # Creamos un objeto tipo cliente llamado u
                    # y le pasamos los elementos de la lista:
                    p = Pedido(
                        lista[0],
                        lista[1],
                        lista[2],
                        lista[3],
                        lista[4],
                        lista[5],
                        lista[6],
                        lista[7],
                        lista[8]
                    )
                    # metemos el objeto en la lista de usuarios:
                    pedidos.append(p)

                # Cerramos el archivo:
                self.file.close()

                # En este punto tenemos la lista usuarios con todos los usuarios:

                # Variable para controlar si ya existe el registro:
                existeRegistro = False

                # Variable para controlar si ya es un registro que ya existe y se va a editar:
                existeNombreCompleto = False



            # si los datos son diferentes a lo que existe:
            if not existeRegistro:

                # Recorre la lista de pedidos
                for p in pedidos:
                    # comparamo todos los datos del registro ingresado ocn el documento:
                    if (p.codigoPedido == self.tabla.item(filaActual, 0).text()):
                        # Indicamos que encontramos el documento
                        existeNombreCompleto = True

                        # Volvemos a actualizar todos los datos del usuario:
                        p.codigoPedido = self.tabla.item(filaActual, 0).text()
                        p.nombreCliente = self.tabla.item(filaActual, 1).text()
                        p.cedulaCliente = self.tabla.item(filaActual,2).text()
                        p.direccion = self.tabla.item(filaActual, 3).text()
                        p.celular = self.tabla.item(filaActual,4).text()
                        p.morcillaCantidad = self.tabla.item(filaActual, 5).text()
                        p.chorizoCantidad = self.tabla.item(filaActual, 6).text()
                        p.arrozCantidad = self.tabla.item(filaActual, 7).text()
                        p.estadoPedido = self.tabla.item(filaActual, 8).text()

                        # abrimos el archivo en modo escritura escribiendo datos en binario.
                        self.file = open('archivos_planos/clientes.txt', 'wb')

                        # recorremos la lista de usuarios
                        # para guardar usuario por usuario en el archivo
                        for p in pedidos:
                            self.file.write(bytes(p.codigoPedido + ";" + p.nombreCliente + ";" + p.cedulaCliente + ";" + p.direccion.strip() + ";" + p.celular.strip() + ";" + p.morcillaCantidad.strip() + ";" + p.chorizoCantidad.strip() + ";" + p.arrozCantidad.strip() + ";" + p.estadoPedido.strip() + "\n", encoding='UTF-8'))

                        self.file.close()

                        return QMessageBox.question(self,
                                                    'Confirmacion',
                                                    'Los datos del pedido se han editado exitosamente.',
                                                    QMessageBox.StandardButton.Ok
                                                )

                        # Paramos el for:
                        break



        if datosVacios:
            return QMessageBox.warning(self, 'Alerta', 'Debe ingresar todos los datos en el registro')


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo ventana 1 con el nombre de ventana 1
    ventana = VentanaHistorialPedidos()

    # hacer que el objeto ventana 1 se vea
    ventana.show()

    # para terminar la aplicacion
    sys.exit(app.exec_())