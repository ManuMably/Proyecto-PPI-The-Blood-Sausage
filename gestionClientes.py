import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QScrollArea, QTableWidget, QVBoxLayout, QLabel, \
    QApplication, QHBoxLayout, \
    QStyle, QTableWidgetItem, QPushButton, QLineEdit, QFormLayout, QToolBar, QAction, QMessageBox, QDialogButtonBox, \
    QDialog

from cliente import Cliente


class GestionClientes(QMainWindow):

    # metodo constructor de la ventana
    def __init__(self, clientes=None):
        super(GestionClientes, self).__init__(clientes)

        # creamos un atributo que guarde la ventana anterior
        self.clientes = clientes

        # Titulo de la ventana
        self.setWindowTitle("Gestionar Clientes")

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
                                          "border-radius: 7px;margin-bottom: 5px; margin-bottom: 50px;")
        self.letreroCelular.setAlignment(Qt.AlignCenter)
        self.letreroCelular.setFixedWidth(200)

        # creamos el campo para el nombre del cliente
        self.celularCliente = QLineEdit()
        self.celularCliente.setFixedWidth(400)
        self.celularCliente.setMaxLength(10)
        self.celularCliente.setStyleSheet("background-color: #ffffff")

        # agregamos el letrero al layout formularioDatosPedido
        self.formularioRegistro.addRow(self.letreroCelular, self.celularCliente)

        # hacemos un boton para buscar clientes y cargar los datos
        self.buscar = QPushButton("Buscar")
        self.buscar.setFixedWidth(150)
        self.buscar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 20px; margin-bottom: 30px;")
        self.buscar.setFont(QFont("Arial", 15))
        self.buscar.clicked.connect(self.accion_buscarCliente)

        self.formularioRegistro.addRow(self.buscar)

        # hacemos un boton para buscar clientes y cargar los datos
        self.editar = QPushButton("Editar")
        self.editar.setFixedWidth(150)
        self.editar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 20px; margin-bottom: 30px;")
        self.editar.setFont(QFont("Arial", 15))
        self.editar.clicked.connect(self.accion_editarCliente)

        # hacemos un boton para buscar clientes y cargar los datos
        self.eliminar = QPushButton("Eliminar")
        self.eliminar.setFixedWidth(150)
        self.eliminar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 20px; margin-bottom: 30px;")
        self.eliminar.setFont(QFont("Arial", 15))
        self.eliminar.clicked.connect(self.accion_eliminarCliente)

        self.formularioRegistro.addRow(self.editar, self.eliminar)

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
        self.clientes.show()

    def accion_buscarCliente(self):

        # variable para controlar que se han ingresado datos correctos
        self.datosCorrectos = True

        self.ventanaDialogo.setWindowTitle("Buscar Cliente")

        # validar que se haya ingresado el documento
        if (self.cedulaCliente.text() == ''):
            self.datosCorrectos = False

            # escribimos texto explicativo
            self.mensaje.setText("Si va a buscar un cliente "
                                 "para cargar sus datos."
                                 "\nDebe primero, ingresar el documento.")

            # hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

        # validar si el documento es numerico
        if (not self.cedulaCliente.text().isnumeric()):
            self.datosCorrectos = False

            # escribimos texto explicativo
            self.mensaje.setText("El documento debe ser numerico."
                                 "\nNo ingrese letras, "
                                 "ni caracteres especiales.")

            # hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

        # si los datos estan correctos
        if (self.datosCorrectos):

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

            # variable para controlar si el documento existe
            existeDocumento = False

            # buscamos en la lista usuario por usuario si existe el documento
            for u in usuarios:

                # comparamos el documento ingresado
                # si corresponde con el documento, es el usuario correcto
                if u.cedula == self.cedulaCliente.text():

                    # mostramos los datos en el formulario
                    self.cedulaCliente.setText(u.cedula)
                    self.cedulaCliente.setReadOnly(True)
                    self.nombreCliente.setText(u.nombreCompleto)
                    self.nombreCliente.setReadOnly(True)
                    self.direccionCliente.setText(u.direccion)
                    self.celularCliente.setText(u.celular)

                    # indicamos que encontramos el documento
                    existeDocumento = True

                    # paramos el for
                    break

            # si no existe un usuario con este documento
            if (not existeDocumento):
                # escribimos un texto expplicativo
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + self.cedulaCliente.text())

                # hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

                self.accion_botonVolver()

    def accion_editarCliente(self):

        # variable para controlar que se han ingresado datos correctos
        self.datosCorrectos = True

        # establecemos el titulo de la ventana
        self.ventanaDialogo.setWindowTitle("Formulario de edicion")

        # validamos que se ingresen todos los campos
        if (
                self.cedulaCliente.text() == ''
                or self.nombreCliente.text() == ''
                or self.direccionCliente.text() == ''
                or self.celularCliente.text() == ''
        ):
            self.datosCorrectos = False

            # texto explicativo
            self.mensaje.setText("Debe seleccionar un cliente con documento valido"
                                 "\ny llenar todos los campos.")

            # para que se vea ventalaDialogo
            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

        # si los datos estan correctos
        if self.datosCorrectos:
            # abrimos el archivo en modo lectura
            self.file = open('archivos_planos/clientes.txt', 'rb')

            # lista vacia para guardar los usuarios
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # obtenemos del string una lista de 11 datos separados por ;
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

            # variable para controlar si el documento existe
            existeDocumento = False

            # buscamos en la lista usuario por usuario si existe el documento
            for u in usuarios:

                # comparamos el documento ingresado
                # si corresponde con el documento, es el usuario correcto
                if str(u.cedula) == self.cedulaCliente.text():

                    # guardamos los datos del formulario en las propiedades del usuario
                    u.direccion = self.direccionCliente.text()
                    u.celular = self.celularCliente.text()

                    # indicamos que encontramos el documento
                    existeDocumento = True
                    # paramos el for
                    break

            # si no existe un usuario con este documento
            if (not existeDocumento):
                # escribimos un texto expplicativo
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + str(self.cedulaCliente))

                # hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

            # si existe documento y se edita correctamente
            if (existeDocumento):

                # abrimos el archivo en modo agregar escribiendo datos en binario
                self.file = open('archivos_planos/clientes.txt', 'wb')

                # recorremos la lista de usuaris
                # para guardar usuario por usuario en el archivo
                for u in usuarios:
                    self.file.write(bytes(u.cedula + ";"
                                          + u.nombreCompleto + ";"
                                          + u.direccion + ";"
                                          + u.celular, encoding='UTF-8'))
                # para cerrar el archivo
                self.file.close()

            
                # escribimos texto explicativo
                self.mensaje.setText("Cliente actualizado correctamente!")

                # hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

                self.accion_botonVolver()

    def accion_eliminarCliente(self):

        # variable para controlar que se han ingresado datos correctos
        self.datosCorrectos = True

        # establecemos el titulo de la ventana
        self.ventanaDialogo.setWindowTitle("Formulario de edicion")

        # validamos que se ingresen todos los campos
        if (
                self.cedulaCliente.text() == ''
                or self.nombreCliente.text() == ''
                or self.direccionCliente.text() == ''
                or self.celularCliente.text() == ''
        ):
            self.datosCorrectos = False

            # texto explicativo
            self.mensaje.setText("Debe seleccionar un cliente con documento valido"
                                 "\ny llenar todos los campos.")

            # para que se vea ventalaDialogo
            self.ventanaDialogo.exec_()

        if self.datosCorrectos:
            # creamos ventana de dialogo para confirmar si vamos a eliminar
            self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

            # definimos el tamaño de la ventana
            self.ventanaDialogo.resize(300, 150)

            # configuramos la ventana para que sea modal
            self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

            # creamos un layout vertical
            self.verticalEliminar = QVBoxLayout()

            # creamos un label para los mensajes
            self.mensajeEliminar = QLabel("¿Esta seguro que desea eliminar este registro?")

            # le ponemos los estilos
            self.mensajeEliminar.setStyleSheet("background-color: #61433f; color: #FFFFFF; padding: 10px;")

            # agregamos el label de mensaje
            self.verticalEliminar.addWidget(self.mensajeEliminar)

            # agregamos las opciones de aceptar y cancelar en la ventana de dialogo
            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)

            # agregamos las opciones de los botones
            self.verticalEliminar.addWidget(self.opcionesBox)

            # establecemos el layout para la ventana
            self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

            # hacemos que la ventana se vea
            self.ventanaDialogoEliminar.exec_()

        if self.eliminar:
            # abrimos el archivo en modo lectura
            self.file = open('archivos_planos/clientes.txt', 'rb')

            # lista vacia para guardar los usuarios
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # obtenemos del string una lista de 11 datos separados por ;
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

            # variable para controlar si el documento existe
            existeDocumento = False

            # buscamos en la lista usuario por usuario si existe el documento
            for u in usuarios:

                # comparamos el documento ingresado
                # si corresponde con el documento, es el usuario correcto
                if str(u.cedula) == self.cedulaCliente.text():
                    # eliminamos el usuario de la lista de usuarios
                    usuarios.remove(u)
                    existeDocumento = True
                    # paramos el for
                    break

            # abrimos el archivo en modo agregar escribiendo datos en binario
            self.file = open('archivos_planos/clientes.txt', 'wb')

            for u in usuarios:
                self.file.write(bytes(u.cedula + ";"
                                      + u.nombreCompleto + ";"
                                      + u.direccion + ";"
                                      + u.celular, encoding='UTF-8'))
            # para cerrar el archivo
            self.file.close()

                # si existe documento y se edito correctamenett
            if (existeDocumento):
                 # escribimos texto explicativo
                self.mensaje.setText("Usuario eliminado exitosamente!")

                # hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()
                self.accion_botonVolver()

    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = False
        self.accion_botonVolver()

if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto del tipo realizarPedido con el nombre de RealizarPedido
    gestionClientes = GestionClientes()

    # hacer que RealizarPedido se vea
    gestionClientes.show()

    # para cerrar la aplicacion
    sys.exit(app.exec_())