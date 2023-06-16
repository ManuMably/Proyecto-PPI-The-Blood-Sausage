import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, \
    QLabel, QFormLayout, QLineEdit, QMessageBox

from pedido import Pedido


class BuscadorPedidos(QMainWindow):

    def __init__(self, anterior=None):
        super(BuscadorPedidos, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.pedidoSolicitado = anterior.pedidoBusqueda
        # generador de la ventana -----------------------------------
        # Titulo de la ventana
        self.setWindowTitle("Buscador De Pedidos")

        # ponemos color de fondo a la ventana
        self.setStyleSheet("background-color: #292828")

        # Ancho y alto de la ventana
        self.ancho = 600
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

        # boton Volver
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 350px; margin-bottom: 50px;")
        self.botonVolver.setFont(QFont("Arial", 15))
        # ponemos el boton volver a funcionar
        self.botonVolver.clicked.connect(self.accion_botonVolver)
        # lo agregamos
        self.verticalCentral.addWidget(self.botonVolver)

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

        # creamos el letrero cedula
        self.letreroCedula = QLabel()
        # texto de letrero
        self.letreroCedula.setText("Cedula:")
        # tipo de letra del letrero
        self.letreroCedula.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroCedula.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                          "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom:5px;")
        self.letreroCedula.setAlignment(Qt.AlignCenter)
        self.letreroCedula.setFixedWidth(200)

        # creamos el campo para el cedula del cliente
        self.cedulaCliente = QLabel()
        self.cedulaCliente.setText("Aqui va la cedula del cliente en el pedido")
        self.cedulaCliente.setFixedWidth(250)
        self.cedulaCliente.setStyleSheet("background-color: #FFFFFF; margin-left: 20px;"
                                          "margin-right: 10px ;color: #61433f; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom: 5px;")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioDatosPedido.addRow(self.letreroCedula, self.cedulaCliente)

        # creamos el letrero Direccion
        self.letreroDireccion = QLabel()
        # texto de letrero
        self.letreroDireccion.setText("Direccion")
        # tipo de letra del letrero
        self.letreroDireccion.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroDireccion.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                         "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                         "border-width: 1px; border-color: #000000;"
                                         "border-radius: 7px;margin-bottom:5px;")
        self.letreroDireccion.setAlignment(Qt.AlignCenter)
        self.letreroDireccion.setFixedWidth(200)

        # creamos el campo para el cedula del cliente
        self.direccionCliente = QLineEdit()
        self.direccionCliente.setFixedWidth(250)
        self.direccionCliente.setStyleSheet("background-color: #FFFFFF; margin-left: 20px;"
                                         "margin-right: 10px ;color: #61433f; border: solid;"
                                         "border-width: 1px; border-color: #000000;"
                                         "border-radius: 7px;margin-bottom: 5px;")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioDatosPedido.addRow(self.letreroDireccion, self.direccionCliente)

        # creamos el letrero Celular
        self.letreroCelular = QLabel()
        # texto de letrero
        self.letreroCelular.setText("Celular:")
        # tipo de letra del letrero
        self.letreroCelular.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroCelular.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                            "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                            "border-width: 1px; border-color: #000000;"
                                            "border-radius: 7px;margin-bottom:5px;")
        self.letreroCelular.setAlignment(Qt.AlignCenter)
        self.letreroCelular.setFixedWidth(200)

        # creamos el campo para el cedula del cliente
        self.celularCliente = QLineEdit()
        self.celularCliente.setFixedWidth(250)
        self.celularCliente.setStyleSheet("background-color: #FFFFFF; margin-left: 20px;"
                                            "margin-right: 10px ;color: #61433f; border: solid;"
                                            "border-width: 1px; border-color: #000000;"
                                            "border-radius: 7px;margin-bottom: 5px;")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioDatosPedido.addRow(self.letreroCelular, self.celularCliente)

        # creamos el letrero Cantidad morcilla
        self.letreroCantidadMorcilla = QLabel()
        # texto de letrero
        self.letreroCantidadMorcilla.setText("Cantidad Morcilla:")
        # tipo de letra del letrero
        self.letreroCantidadMorcilla.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroCantidadMorcilla.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                          "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom:5px;")
        self.letreroCantidadMorcilla.setAlignment(Qt.AlignCenter)
        self.letreroCantidadMorcilla.setFixedWidth(200)

        # creamos el campo para el cedula del cliente
        self.morcillaCliente = QLineEdit()
        self.morcillaCliente.setFixedWidth(250)
        self.morcillaCliente.setStyleSheet("background-color: #FFFFFF; margin-left: 20px;"
                                          "margin-right: 10px ;color: #61433f; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom: 5px;")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioDatosPedido.addRow(self.letreroCantidadMorcilla, self.morcillaCliente)

        # creamos el letrero Cantidad chorizo
        self.letreroCantidadChorizo = QLabel()
        # texto de letrero
        self.letreroCantidadChorizo.setText("Cantidad Chorizo:")
        # tipo de letra del letrero
        self.letreroCantidadChorizo.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroCantidadChorizo.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                          "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom:5px;")
        self.letreroCantidadChorizo.setAlignment(Qt.AlignCenter)
        self.letreroCantidadChorizo.setFixedWidth(200)

        # creamos el campo para el cedula del cliente
        self.chorizoCliente = QLineEdit()
        self.chorizoCliente.setFixedWidth(250)
        self.chorizoCliente.setStyleSheet("background-color: #FFFFFF; margin-left: 20px;"
                                          "margin-right: 10px ;color: #61433f; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom: 5px;")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioDatosPedido.addRow(self.letreroCantidadChorizo, self.chorizoCliente)

        # creamos el letrero Cantidad Arroz
        self.letreroCantidadArroz = QLabel()
        # texto de letrero
        self.letreroCantidadArroz.setText("Cantidad Arroz:")
        # tipo de letra del letrero
        self.letreroCantidadArroz.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroCantidadArroz.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                          "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom:5px;")
        self.letreroCantidadArroz.setAlignment(Qt.AlignCenter)
        self.letreroCantidadArroz.setFixedWidth(200)

        # creamos el campo para el cedula del cliente
        self.arrozCliente = QLineEdit()
        self.arrozCliente.setFixedWidth(250)
        self.arrozCliente.setStyleSheet("background-color: #FFFFFF; margin-left: 20px;"
                                          "margin-right: 10px ;color: #61433f; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom: 5px;")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioDatosPedido.addRow(self.letreroCantidadArroz, self.arrozCliente)

        # creamos el letrero estado del pedido
        self.letreroEstadoPedido = QLabel()
        # texto de letrero
        self.letreroEstadoPedido.setText("Estado pedido:")
        # tipo de letra del letrero
        self.letreroEstadoPedido.setFont(QFont("Arial", 15))
        # le ponemos los estilos
        self.letreroEstadoPedido.setStyleSheet("background-color: #61433f; margin-left: 20px;"
                                          "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom:5px;")
        self.letreroEstadoPedido.setAlignment(Qt.AlignCenter)
        self.letreroEstadoPedido.setFixedWidth(200)

        # creamos el campo para el cedula del cliente
        self.estadoCliente = QLineEdit()
        self.estadoCliente.setFixedWidth(250)
        self.estadoCliente.setStyleSheet("background-color: #FFFFFF; margin-left: 20px;"
                                          "margin-right: 10px ;color: #61433f; border: solid;"
                                          "border-width: 1px; border-color: #000000;"
                                          "border-radius: 7px;margin-bottom: 5px;")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioDatosPedido.addRow(self.letreroEstadoPedido, self.estadoCliente)

        # agregamos los datos del pedido actual al formulario
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

        # En este punto tenemos la lista pedidos con todos los pedidos

        for p in self.pedidos:
            # buscamos el usuario por el nombre:
            if (p.codigoPedido == self.pedidoSolicitado):
                self.codigoPedidoN.setText(p.codigoPedido)
                self.nombreCliente.setText(p.nombreCliente)
                self.cedulaCliente.setText(p.cedulaCliente)
                self.direccionCliente.setText(p.direccion)
                self.celularCliente.setText(p.celular)
                self.morcillaCliente.setText(p.morcillaCantidad)
                self.chorizoCliente.setText(p.chorizoCantidad)
                self.arrozCliente.setText(p.arrozCantidad)
                self.estadoCliente.setText(p.estadoPedido)


                # paramos el for:
                break






        # ------------BLoque Botones ------------------------------------------------
        # hacemos el boton para Actualizar el pedido
        self.botonActualizarPedido = QPushButton("Actualizar Pedido")

        # establecemos el ancho del boton
        self.botonActualizarPedido.setFixedWidth(300)
        self.botonActualizarPedido.setFixedHeight(50)

        # le ponemos los estilos
        self.botonActualizarPedido.setStyleSheet("background-color: #515670; margin-left: 20px;"
                                        "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                        "border-radius: 15px;margin-bottom:5px;")

        self.botonActualizarPedido.setFont(QFont("Arial", 15))

        self.botonActualizarPedido.clicked.connect(self.accion_botonActualizarPedido)

        self.formularioDatosPedido.addRow(self.botonActualizarPedido)

        # ----------hacemos el boton para guardar la orden -------------------------------------
        self.botonEliminarPedido = QPushButton("Eliminar Pedido")

        # establecemos el ancho del boton
        self.botonEliminarPedido.setFixedWidth(300)
        self.botonEliminarPedido.setFixedHeight(50)

        # le ponemos los estilos
        self.botonEliminarPedido.setStyleSheet("background-color: #515670; margin-left: 20px;"
                                        "margin-right: 10px ;color: #FFFFFF; border: solid;"
                                        "border-radius: 15px;margin-bottom:5px;")

        self.botonEliminarPedido.setFont(QFont("Arial", 15))
        self.botonEliminarPedido.clicked.connect(self.accion_botonEliminarPedido)
        self.formularioDatosPedido.addRow(self.botonEliminarPedido)

        self.verticalCentral.addWidget(self.datosPedido)

        # -------------------------- fin formulario nombre, celular y reiniciar orden --------------------











        # ------------------------- poner al ultimo del constructor -------------------------
        # establecemos verticalCentral como layout del centralInicioSesion
        self.centralBuscadorPedidos.setLayout(self.verticalCentral)


    def accion_botonEliminarPedido(self):
        boton = QMessageBox.question(self,
                                     'Confirmacion',
                                     '¿Esta seguro de que quieres borrar este registro?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                                     )

        if boton == QMessageBox.StandardButton.Yes:
            # Abrimos el archivo en modo de lectura:
            self.file = open('archivos_planos/pedidos.txt', 'rb')

            # lista vacia para guardar los usuarios:
            self.pedidos3 = []

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
                self.pedidos3.append(p)

            # cerramos el archivo:
            self.file.close()

            # en este punto tenemos la lista usuarios con todos los usuarios:

            # Recorremos la lista de usuarios
            for p in self.pedidos3:
                # buscamos el usuario por el nombre:
                if (
                        p.codigoPedido == self.codigoPedidoN.text()
                ):
                    # Removemos el usuario de la lista de usuarios:
                    self.pedidos3.remove(p)

                    # paramos el for:
                    break

            # Abrimos el archivo en modo escritura para reescribir los datos sin el usuario borrado.
            self.file = open('archivos_planos/pedidos.txt', 'wb')

            # recorremos la lista de usuarios
            # para guardar usuario por usuario en el archivo
            for p in self.pedidos3:
                self.file.write(bytes(
                    p.codigoPedido + ";" + p.cedulaCliente.strip() + ";" + p.nombreCliente + ";" + p.direccion.strip() + ";" + p.celular.strip() + ";" + p.morcillaCantidad.strip() + ";" + p.chorizoCantidad.strip() + ";" + p.arrozCantidad.strip() + ";" + p.estadoPedido.strip() + "\n",
                    encoding='UTF-8'))
            self.file.close()
            self.hide()
            self.ventanaAnterior.show()



    def accion_botonVolver(self):
            self.hide()
            self.ventanaAnterior.show()

    def accion_botonActualizarPedido(self):
        self.datosVacios = True

        if (
                self.direccionCliente != '' and
                self.cedulaCliente != '' and
                self.morcillaCliente != '' and
                self.chorizoCliente != '' and
                self.arrozCliente != '' and
                self.estadoCliente != ''
        ):
            # Actualizamos la variable para indicar que se ingresaron todos los datos:
            self.datosVacios = False

            # Abrimos el archivo en modo de lectura:
            self.file = open('archivos_planos/pedidos.txt', 'rb')

            # lista vacia para guardar los usuarios:
            self.pedidos2 = []

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
                self.pedidos2.append(p)

            # Cerramos el archivo:
            self.file.close()

            # En este punto tenemos la lista usuarios con todos los pedidos
            # Recorre la lista de pedidos
            for p in self.pedidos2:
                # comparamo todos los datos del registro ingresado ocn el documento:
                if (p.codigoPedido == self.codigoPedidoN.text()):

                    # Volvemos a actualizar todos los datos del pedido:
                    p.direccion = self.direccionCliente.text()
                    p.celular = self.celularCliente.text()
                    p.morcillaCantidad = self.morcillaCliente.text()
                    p.chorizoCantidad = self.chorizoCliente.text()
                    p.arrozCantidad = self.arrozCliente.text()
                    p.estadoPedido = self.estadoCliente.text()

                    # abrimos el archivo en modo escritura escribiendo datos en binario.
                    self.file = open('archivos_planos/pedidos.txt', 'wb')

                    # recorremos la lista de usuarios
                    # para guardar usuario por usuario en el archivo
                    for p in self.pedidos2:
                        self.file.write(bytes(p.codigoPedido + ";" + p.nombreCliente + ";" + p.cedulaCliente + ";" + p.direccion.strip() + ";" + p.celular.strip() + ";" + p.morcillaCantidad.strip() + ";" + p.chorizoCantidad.strip() + ";" + p.arrozCantidad.strip() + ";" + p.estadoPedido.strip() + "\n", encoding='UTF-8'))

                    self.file.close()
                    # Paramos el for:
                    break
        self.hide()
        self.ventanaAnterior.show()









if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto del tipo iniciar sesion con el nombre de inicioSesion
    buscadorPedidos = BuscadorPedidos()

    # hacer que inicioSesion se vea
    buscadorPedidos.show()

    # para cerrar la aplicacion
    sys.exit(app.exec_())