import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, \
    QWidget, QFormLayout, QLineEdit

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

        # ------------------------------------------------------------------------------
        # TABLA: imagen de lo que sera la tabla de historial de pedidos
        self.tablaHistorialPedidos = QLabel()
        self.imagenTabla = QPixmap("imagenes/ejemploTabla.PNG")
        self.tablaHistorialPedidos.setPixmap(self.imagenTabla)
        self.tablaHistorialPedidos.setAlignment(Qt.AlignHCenter)
        self.tablaHistorialPedidos.setFixedHeight(200)

        # agregamos la tabla a el horizontalTablaYFormulario
        self.verticalPrincipal.addWidget(self.tablaHistorialPedidos)

        # ------------------- Bloque modificacion de pedidos ---------------------------
        self.modificarPedido = QLabel()
        self.modificarPedido.setAlignment(Qt.AlignCenter)
        self.layoutModificarPedido = QHBoxLayout()

        # ------------------ entrada de datos ------------------------------------------
        self.entradaDatosModificacion = QLabel()
        self.imagenEntrada = QPixmap("imagenes/miniaturaSeleccionProducto.JPG")
        self.entradaDatosModificacion.setPixmap(self.imagenEntrada)
        # establecemos que se pueda escalar la imagen
        self.entradaDatosModificacion.setScaledContents(True)
        # el tamaño de la imagen se adapta a la ventana
        self.resize(self.entradaDatosModificacion.width(), self.entradaDatosModificacion.height())
        self.entradaDatosModificacion.setAlignment(Qt.AlignHCenter)
        # agregamos la entrada de datos al layout modificar pedido
        self.layoutModificarPedido.addWidget(self.entradaDatosModificacion)
        # ------------------ Botones ---------------------------------------------------
        self.botonesModificarPedido = QLabel()
        self.botonesModificarPedido.setAlignment(Qt.AlignCenter)
        self.layoutBotonesModificacion = QVBoxLayout()

        # boton Actualizar
        self.botonActualizar = QPushButton("Actualizar")
        self.botonActualizar.setStyleSheet("border-radius: 10px; background-color: #515670; color: #ffffff; margin-left: 30px; margin-right: 30px; margin-bottom: 10px; margin-top: 0px;")
        self.botonActualizar.setFont(QFont("Arial", 15))
        self.layoutBotonesModificacion.addWidget(self.botonActualizar)
        # boton Eliminar
        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setStyleSheet("border-radius: 10px; background-color: #515670; color: #ffffff; margin-left: 30px; margin-right: 30px; margin-bottom: 10px; margin-top: 0px;")
        self.botonEliminar.setFont(QFont("Arial", 15))
        self.layoutBotonesModificacion.addWidget(self.botonEliminar)


        # establecemos el layout de los botones
        self.botonesModificarPedido.setLayout(self.layoutBotonesModificacion)
        # agregamos los botones a el bloque modificacion de pedidos
        self.layoutModificarPedido.addWidget(self.botonesModificarPedido)


        # establecemos el layout del bloque modificarPedido
        self.modificarPedido.setLayout(self.layoutModificarPedido)
        # agregamos el bloque modificarPedido a la vertical principal
        self.verticalPrincipal.addWidget(self.modificarPedido)



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