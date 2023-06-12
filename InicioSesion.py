import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QWidget, QVBoxLayout, QLabel, QFormLayout, \
    QLineEdit, QPushButton, QDialog, QDialogButtonBox, QMessageBox
from PyQt5 import uic, QtWidgets
from PyQt5.uic.properties import QtCore

from empleado import Empleado
from menuPrincipal import MenuPrincipal


class IniciarSesion(QMainWindow):

    def __init__(self, parent=None):
        super(IniciarSesion, self).__init__(parent)

        # Titulo de la ventana
        self.setWindowTitle("Inicio de Sesion")

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

        # imagen logo
        self.labelLogo = QLabel()
        self.logo = QPixmap('imagenes/logoSausage.png')
        self.labelLogo.setFixedHeight(200)
        self.labelLogo.setPixmap(self.logo)
        self.labelLogo.setAlignment(Qt.AlignHCenter)
        # agregamos la imagen al layout principal
        self.verticalCentral.addWidget(self.labelLogo)

        # creamos el letrero de inicio de sesion
        self.letreroInicioSesion = QLabel()
        # texto de letreroInicioSesion
        self.letreroInicioSesion.setText("Inicio de Sesion")
        # tipo de letra del letrero
        self.letreroInicioSesion.setFont(QFont("Arial", 25))
        # estilo del letreto
        self.letreroInicioSesion.setStyleSheet("color: #ffffff;")
        self.letreroInicioSesion.setFixedHeight(100)
        #centrar el texto
        self.letreroInicioSesion.setAlignment(Qt.AlignCenter)

        # agregamos el letreroInicioSesion al layout principal
        self.verticalCentral.addWidget(self.letreroInicioSesion)

        #formulario para iniciar sesion
        self.formularioInicio = QLabel()
        self.formularioInicio.setAlignment(Qt.AlignCenter)
        self.layoutInicioSesion = QFormLayout()

        # label preguntando el usuario
        self.labelUsuario = QLabel("Usuario")
        # tipo de letra del letrero
        self.labelUsuario.setFont(QFont("Arial", 15))
        # estilo label
        self.labelUsuario.setStyleSheet("background-color: #61433f; margin-left: 230px; margin-right: 230px ;color: #ffffff; border: solid; border-width: 1px;"
                                        "border-color: #000000; border-radius: 7px; margin-bottom:5px;")
        self.labelUsuario.setAlignment(Qt.AlignCenter)
        self.layoutInicioSesion.addRow(self.labelUsuario)
        # espacio para el ingreso del usuario
        self.ingresoUsuario = QLineEdit()
        self.ingresoUsuario.setStyleSheet("background-color: #ffffff; margin-left:200px; margin-right: 200px ;color: #000000; border: solid; border-width: 1px;"
                                        "border-color: #000000; border-radius: 7px;margin-bottom:10px;")
        self.layoutInicioSesion.addRow(self.ingresoUsuario)

        # label preguntando el la contraseña
        self.labelContrasena = QLabel("Contraseña")
        # tipo de letra del letrero
        self.labelContrasena.setFont(QFont("Arial", 15))
        # estilo label
        self.labelContrasena.setStyleSheet("background-color: #61433f; margin-left: 230px; margin-right: 230px ;color: #ffffff; border: solid; border-width: 1px;"
                                        "border-color: #000000; border-radius: 7px;margin-bottom:5px;")
        self.labelContrasena.setAlignment(Qt.AlignCenter)
        self.layoutInicioSesion.addRow(self.labelContrasena)
        # espacio para ingreso de contraseña
        self.ingresoContrasena = QLineEdit()
        self.ingresoContrasena.setEchoMode(QLineEdit.Password)
        self.ingresoContrasena.setStyleSheet("background-color: #ffffff; margin-left:200px; margin-right: 200px ;color: #000000; border: solid; border-width: 1px;"
                                          "border-color: #000000; border-radius: 7px;margin-bottom:15px;")
        self.layoutInicioSesion.addRow(self.ingresoContrasena)

        # boton ingresar
        self.botonIngresar = QPushButton("Ingresar")
        # tipo de letra del letrero
        self.botonIngresar.setFont(QFont("Arial", 13))
        # estilo del boton
        self.botonIngresar.setStyleSheet("background-color: #515670; margin-left: 200px; margin-right: 200px ;color: #ffffff; border: solid; border-width: 1px;"
                                          "border-color: #000000; border-radius: 7px;")
        self.botonIngresar.clicked.connect(self.abrir)
        # agregamos el boton al formulario
        self.layoutInicioSesion.addRow(self.botonIngresar)




        # layot de formulario inicio de sesion
        self.formularioInicio.setLayout(self.layoutInicioSesion)

        # agregamos el formulario al verticalCentral
        self.verticalCentral.addWidget(self.formularioInicio)







        # establecemos verticalCentral como layout del centralInicioSesion
        self.centralInicioSesion.setLayout(self.verticalCentral)

    def abrir (self):

        # variable para controlar que se han ingresado datos correctos
        self.datosCorrectos = True

        # validar que se haya ingresado el usuario
        if(self.ingresoUsuario.text() == ''):
            self.datosCorrectos = False
            # mensaje por error en los datos ingresados
            self.alerta = QMessageBox()
            self.alerta.setIcon(QMessageBox.Warning)
            self.alerta.setWindowTitle("Alerta")
            self.alerta.setText("Para ingresar debes poner un usuario y contraseña.")
            self.alerta.setStandardButtons(QMessageBox.Ok)
            self.alerta.exec_()

        if(self.datosCorrectos):
            # abrimos el archivo en modo lectura
            self.file = open('archivos_planos/empleadosRegistrados.txt', 'rb')

            # lista vacia para guardar los empleados
            empleados = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # obtenemos del string una lista de 3 datos separados por ;
                lista = linea.split(";")

                # se para si ya no hay registros en el archivo
                if linea == '':
                    break

                # creamos un objeto tipo empleado llamado e
                e = Empleado(lista[0], lista[1], lista[2])

                # metemos el objeto en la lista empleados
                empleados.append(e)

            # cerramos el archivo
            self.file.close()

            # ya tenemos la lista con todos los empleados

            # variable para controlar si el empleado existe
            existeEmpleado= False

            # Buscamos en la lista empleado por empleado si existe el nombreEmpleado
            for e in empleados:

                # comparamos el usuario ingresado
                # si corresponde con nombreEmpleado, es el empleado correcto
                if (e.nombreEmpleado == self.ingresoUsuario.text() and e.contrasena == self.ingresoContrasena.text()):

                    print("se ha ingresado el usuario y contraseña correcto")
                    self.hide()
                    self.menuPrincipal = MenuPrincipal(self)
                    self.menuPrincipal.show()

                    # indicamos que encontramos el usuario
                    existeEmpleado = True

                    # paramos el for
                    break

            # si no existe el usuario
            if(not existeEmpleado):
                # mensaje por que no se encuentra el empleado registrado
                self.alerta = QMessageBox()
                self.alerta.setIcon(QMessageBox.Warning)
                self.alerta.setWindowTitle("Alerta")
                self.alerta.setText("El empleado no se encuentra registrado o has escrito mal el usuario y contraseña.")
                self.alerta.setStandardButtons(QMessageBox.Ok)
                self.alerta.exec_()



if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto del tipo iniciar sesion con el nombre de inicioSesion
    inicioSesion = IniciarSesion()

    # hacer que inicioSesion se vea
    inicioSesion.show()

    # para cerrar la aplicacion
    sys.exit(app.exec_())
