import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QScrollArea, QTableWidget, QVBoxLayout, QLabel, QApplication, QHBoxLayout, \
    QStyle, QTableWidgetItem, QPushButton, QLineEdit, QFormLayout, QToolBar, QAction, QMessageBox

from cliente import Cliente

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

        """# ________________MENU TOOLBAR_______________________________

        self.toolbar = QToolBar('Main toolbar')
        self.toolbar.setIconSize(QSize(92, 92))
        self.toolbar.setStyleSheet("margin-left: 50px;")
        self.addToolBar(self.toolbar)

        # ---------- add ---------
        self.add = QAction(QIcon('imagenes/iconos/add.png'), '&Crear', self)
        self.add.triggered.connect(self.accion_add)
        self.toolbar.addAction(self.add)

        # ---------- insert ------------
        self.insert = QAction(QIcon('imagenes/iconos/edit.png'), '&Editar', self)
        self.insert.triggered.connect(self.accion_insert)
        self.toolbar.addAction(self.insert)

        # -------------- delete ----------
        self.delete = QAction(QIcon('imagenes/iconos/delete.png'), '&Eliminar', self)
        self.delete.triggered.connect(self.accion_delete)
        self.toolbar.addAction(self.delete)

        self.verticalCentral.addWidget(self.toolbar)"""
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
        self.botonRegistrar.clicked.connect(self.accion_add)
        # lo agregamos
        self.layoutBloqueBotones.addWidget(self.botonRegistrar)

        # boton Cambiar
        self.botonCambiar = QPushButton("Actualizar")
        self.botonCambiar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 35px; margin-bottom: 150px;")
        self.botonCambiar.setFont(QFont("Arial", 15))
        # ponemos el boton actualizar a funcionar
        self.botonCambiar.clicked.connect(self.accion_insert)
        # lo agregamos
        self.layoutBloqueBotones.addWidget(self.botonCambiar)

        # boton Eliminar
        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setStyleSheet(
            "border-radius: 10px; background-color: #515670;color: #ffffff; margin-left: 50px; margin-right: 35px; margin-bottom: 150px;")
        self.botonEliminar.setFont(QFont("Arial", 15))
        # ponemos el boton Eliminar a funcionar
        self.botonEliminar.clicked.connect(self.accion_delete)
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
                self.file = open('archivos_planos/clientes.txt', 'rb')

                # lista vacia para guardar los usuarios:
                usuarios = []

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
                    u = Cliente(
                        lista[0],
                        lista[1],
                        lista[2],
                    )
                    # metemos el objeto en la lista de usuarios:
                    usuarios.append(u)

                # cerramos el archivo:
                self.file.close()

                # en este punto tenemos la lista usuarios con todos los usuarios:

                # Recorremos la lista de usuarios
                for u in usuarios:
                    # buscamos el usuario por el nombre:
                    if (
                            u.nombreCompleto == self.tabla.item(filaActual, 0).text()
                    ):

                        # Removemos el usuario de la lista de usuarios:
                        usuarios.remove(u)

                        # paramos el for:
                        break

                # Abrimos el archivo en modo escritura para reescribir los datos sin el usuario borrado.
                self.file = open('archivos_planos/clientes.txt', 'wb')

                # recorremos la lista de usuarios
                # para guardar usuario por usuario en el archivo
                for u in usuarios:
                    self.file.write(bytes(u.nombreCompleto + ";"
                                          + u.direccion + ";"
                                          + u.celular, encoding='UTF-8'))
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


    def accion_add(self):

        # Obtenemos el numero de filas que tiene la tabla:
        ultimaFila = self.tabla.rowCount()

        # Insertamos una fila nueva despues de la ultima fila:
        self.tabla.insertRow(ultimaFila)

        # llenamos cada celda de la nueva fila con un string vacio '':
        self.tabla.setItem(ultimaFila, 0, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 1, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 2, QTableWidgetItem(''))

    def accion_insert(self):

        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self, 'Alerta', 'Para ingresar, debe seleccionar un registro')

        boton = QMessageBox.question(self,
                                    'Confirmacion',
                                    '¿Esta seguro de que quiere ingresar este nuevo registro?',
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
                self.file = open('archivos_planos/clientes.txt', 'rb')

                # lista vacia para guardar los usuarios:
                usuarios = []

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
                    u = Cliente(
                        lista[0],
                        lista[1],
                        lista[2],
                    )
                    # metemos el objeto en la lista de usuarios:
                    usuarios.append(u)

                # Cerramos el archivo:
                self.file.close()

                # En este punto tenemos la lista usuarios con todos los usuarios:

                # Variable para controlar si ya existe el registro:
                existeRegistro = False

                # Variable para controlar si ya es un registro que ya existe y se va a editar:
                existeNombreCompleto = False

                # recorremos la lista de usuarios
                for u in usuarios:
                    # comparamos todos los datos del registro ingresado:
                    if (
                            u.nombreCompleto == self.tabla.item(filaActual, 0).text() and
                            u.direccion == self.tabla.item(filaActual, 1).text() and
                            u.celular == self.tabla.item(filaActual, 2).text()
                    ):
                        # Indicamos que encontramos el docuemnto:
                        existeRegistro = True

                        return QMessageBox.warning(self, 'Alerta', 'Registro duplicado, no se puede registrar')

                        # Paramos el for:
                        break

            # si los datos son diferentes a lo que existe:
            if not existeRegistro:

                # Recorre la lista de usuarios
                for u in usuarios:
                    # comparamo todos los datos del registro ingresado ocn el documento:
                    if (u.nombreCompleto == self.tabla.item(filaActual, 0).text()):
                        # Indicamos que encontramos el documento
                        existeNombreCompleto = True

                        # Volvemos a actualizar todos los datos del usuario:
                        u.nombreCompleto = self.tabla.item(filaActual, 0).text()
                        u.direccion = self.tabla.item(filaActual, 1).text()
                        u.celular = self.tabla.item(filaActual, 2).text()

                        # abrimos el archivo en modo escritura escribiendo datos en binario.
                        self.file = open('archivos_planos/clientes.txt', 'wb')

                        # recorremos la lista de usuarios
                        # para guardar usuario por usuario en el archivo
                        for u in usuarios:
                            self.file.write(bytes(u.nombreCompleto + ";"
                                                  + u.direccion + ";"
                                                  + u.celular, encoding='UTF-8'))

                        self.file.close()

                        return QMessageBox.question(self,
                                                    'Confirmacion',
                                                    'Los datos del registro se han editado exitosamente.',
                                                    QMessageBox.StandardButton.Ok
                                                )

                        # Paramos el for:
                        break

                # si se trata de un usuario nuevo:
                if not existeNombreCompleto:
                    # Abrimos el archivo en modo agregar escribiendo datos en binario.
                    self.file = open('archivos_planos/clientes.txt', 'ab')

                    # agregamos los datos de la fila en el archivo
                    self.file.write(bytes(self.tabla.item(filaActual, 0).text() + ";" +
                                          self.tabla.item(filaActual, 1).text() + ";" +
                                          self.tabla.item(filaActual, 2).text() + "\n", encoding='UTF-8'))
                    self.file.seek(0, 2)
                    self.file.close()

                return QMessageBox.question(self,
                                            'Confirmacion',
                                            'Los datos del registro se han ingresado exitosamente.',
                                            QMessageBox.StandardButton.Ok
                                        )

        if datosVacios:
            return QMessageBox.warning(self, 'Alerta', 'Debe ingresar todos los datos en el registro')


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto del tipo realizarPedido con el nombre de RealizarPedido
    clientes = Clientes()

    # hacer que RealizarPedido se vea
    clientes.show()

    # para cerrar la aplicacion
    sys.exit(app.exec_())