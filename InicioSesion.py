import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QWidget, QVBoxLayout, QLabel, QFormLayout, \
    QLineEdit, QPushButton
from PyQt5 import uic, QtWidgets
from menuPrincipal import MenuPrincipal


class IniciarSesion(QMainWindow):

    def __init__(self, parent=None):
        super(IniciarSesion, self).__init__(parent)

        # Titulo de la ventana
        self.setWindowTitle("Inicio de Sesion")

        # ponemos color de fondo a la ventana
        self.setStyleSheet("background-color: #e6ebe0")

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
        self.letreroInicioSesion.setStyleSheet("color: black;")
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
        self.labelUsuario.setStyleSheet("background-color: #ffffff; margin-left: 230px; margin-right: 230px ;color: #000000; border: solid; border-width: 1px;"
                                        "border-color: #000000; border-radius: 7px; margin-bottom:5px;")
        self.labelUsuario.setAlignment(Qt.AlignCenter)
        self.layoutInicioSesion.addRow(self.labelUsuario)
        # espacio para el ingreso del usuario
        self.ingresoUsuario = QLineEdit()
        self.ingresoUsuario.setStyleSheet("background-color: #ed6a5a; margin-left:200px; margin-right: 200px ;color: #000000; border: solid; border-width: 1px;"
                                        "border-color: #000000; border-radius: 7px;margin-bottom:10px;")
        self.layoutInicioSesion.addRow(self.ingresoUsuario)

        # label preguntando el la contraseña
        self.labelContrasena = QLabel("Contraseña")
        # tipo de letra del letrero
        self.labelContrasena.setFont(QFont("Arial", 15))
        # estilo label
        self.labelContrasena.setStyleSheet("background-color: #ffffff; margin-left: 230px; margin-right: 230px ;color: #000000; border: solid; border-width: 1px;"
                                        "border-color: #000000; border-radius: 7px;margin-bottom:5px;")
        self.labelContrasena.setAlignment(Qt.AlignCenter)
        self.layoutInicioSesion.addRow(self.labelContrasena)
        # espacio para ingreso de contraseña
        self.ingresoContrasena = QLineEdit()
        self.ingresoContrasena.setStyleSheet("background-color: #ed6a5a; margin-left:200px; margin-right: 200px ;color: #000000; border: solid; border-width: 1px;"
                                          "border-color: #000000; border-radius: 7px;margin-bottom:15px;")
        self.layoutInicioSesion.addRow(self.ingresoContrasena)

        # boton ingresar
        self.botonIngresar = QPushButton("Ingresar")
        # tipo de letra del letrero
        self.botonIngresar.setFont(QFont("Arial", 13))
        # estilo del boton
        self.botonIngresar.setStyleSheet("background-color: #36c9c6; margin-left: 200px; margin-right: 200px ;color: #000000; border: solid; border-width: 1px;"
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
        self.menuPrincipal = MenuPrincipal(self)
        self.menuPrincipal.show()


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto del tipo iniciar sesion con el nombre de inicioSesion
    inicioSesion = IniciarSesion()

    # hacer que inicioSesion se vea
    inicioSesion.show()

    # para cerrar la aplicacion
    sys.exit(app.exec_())
