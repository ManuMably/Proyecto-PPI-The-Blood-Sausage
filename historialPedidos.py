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
        # bloque titulo y boton volver

        # widget que almacena el boton volver y el titulo
        self.volverYTitulo = QWidget()
        # definimos el layout del widget volverYTitulo
        self.horizontalVolverTitulo = QHBoxLayout()
        # asignamos el layout de volverYTitulo
        self.volverYTitulo.setLayout(self.horizontalVolverTitulo)

        # organizacion del boton volver y titulo
        self.horizontalVolverTitulo.setContentsMargins(0, 0, 0, 0)
        self.horizontalVolverTitulo.setSpacing(0)

        # boton volver
        self.botonVolver = QPushButton("Volver")
        # estilo boton volver
        self.botonVolver.setStyleSheet("background-color: #515670; color: #ffffff; border-radius: 30px; margin-right: 300px")
        self.botonVolver.setFont(QFont("Arial", 20))
        self.botonVolver.setFixedSize(400, 60)
        self.botonVolver.setContentsMargins(0, 0, 0, 0)
        # ponemos el boton volver a funcionar
        self.botonVolver.clicked.connect(self.accion_botonVolver)

        # agregamos al widget el boton volver
        self.horizontalVolverTitulo.addWidget(self.botonVolver)

        # letrero titulo historial de pedidos
        self.letreroHistorialPedidos = QLabel()
        self.letreroHistorialPedidos.setText("Historial de Pedidos")
        self.letreroHistorialPedidos.setStyleSheet("background-color: #61433f; color: #ffffff; border-radius: 30px; margin-left: 200px")
        self.letreroHistorialPedidos.setFont(QFont("Arial", 20))
        self.letreroHistorialPedidos.setFixedSize(500, 60)
        self.letreroHistorialPedidos.setAlignment(Qt.AlignCenter)
        self.horizontalVolverTitulo.addWidget(self.letreroHistorialPedidos)

        # margen de la vertical principal
        self.verticalPrincipal.setContentsMargins(0, 0, 0, 0)
        self.verticalPrincipal.setSpacing(0)
        # agregamos el widget de volverYTitulo
        self.verticalPrincipal.addWidget(self.volverYTitulo)

        # ------------------------------------------------------------------------------
        # bloque tabla y formulario

        # widget donde se ubican la tabla y el formulario
        self.tablaYFormulario = QWidget()
        # layout del widget tablaYFormulario
        self.horizontalTablaYFormulario = QHBoxLayout()
        self.tablaYFormulario.setLayout(self.horizontalTablaYFormulario)

        # organizacion de Bloque Tabla y Formulario
        self.horizontalTablaYFormulario.setContentsMargins(20, 0, 20, 50)
        self.horizontalTablaYFormulario.setSpacing(0)

        # TABLA: imagen de lo que sera la tabla de historial de pedidos
        self.tablaHistorialPedidos = QLabel()
        self.imagenTabla = QPixmap("imagenes/ejemploTabla.PNG")
        self.tablaHistorialPedidos.setPixmap(self.imagenTabla)

        # agregamos la tabla a el horizontalTablaYFormulario
        self.horizontalTablaYFormulario.addWidget(self.tablaHistorialPedidos)

        # FORMULARIO:
        # establecemos el formulario y el layout del formulario
        self.formularioEditarPedido = QWidget()
        self.formularioLayout = QFormLayout()
        self.formularioEditarPedido.setLayout(self.formularioLayout)

        # label y entrada de nombreCliente
        self.nombreCliente = QLabel()
        self.nombreCliente.setText("Nombre: ")
        self.nombreCliente.setStyleSheet("background-color: #61433f; color: #ffffff; margin-bottom: 10px; margin-left: 10px")
        self.nombreCliente.setFont(QFont("Arial", 15))
        self.entradaNombreClientre = QLineEdit()
        # agregamos label y entrada cliente a formularioLayout
        self.formularioLayout.addRow(self.nombreCliente, self.entradaNombreClientre)

        # label y entrada de direccionCliente
        self.direccionCliente = QLabel()
        self.direccionCliente.setText("Direccion: ")
        self.direccionCliente.setStyleSheet("background-color: #61433f; color: #ffffff; margin-bottom: 10px; margin-left: 10px")
        self.direccionCliente.setFont(QFont("Arial", 15))
        self.entradaDireccionClientre = QLineEdit()
        # agregamos label y entrada direccionCliente a formularioLayout
        self.formularioLayout.addRow(self.direccionCliente, self.entradaDireccionClientre)

        # label y entrada de telefonoClientre
        self.telefonoCliente = QLabel()
        self.telefonoCliente.setText("Telefono: ")
        self.telefonoCliente.setStyleSheet("background-color: #61433f; color: #ffffff; margin-bottom: 10px; margin-left: 10px")
        self.telefonoCliente.setFont(QFont("Arial", 15))
        self.entradaTelefonoClientre = QLineEdit()
        # agregamos label y entrada telefonoCliente a formularioLayout
        self.formularioLayout.addRow(self.telefonoCliente, self.entradaTelefonoClientre)

        # seleccion de productos: una imagen de lo que sera la seleccion de productos y cambio en la cantidad
        self.productosCantidad = QLabel()
        self.imagenProductosCantidad = QPixmap("imagenes/miniaturaSeleccionProducto.PNG")
        self.productosCantidad.setPixmap(self.imagenProductosCantidad)
        # agregamos la tabla productosCantidad a formularioLayout
        self.formularioLayout.addRow(self.productosCantidad)

        # checkboxEstadoPedido : por ahora una imagen
        self.estadoPedido = QLabel()
        self.estadoPedido.setText("Estado: ")
        self.estadoPedido.setStyleSheet("margin-bottom: 10px; margin-left: 10px")
        self.estadoPedido.setFont(QFont("Arial", 15))
        self.checkboxEstadoPedido = QLabel()
        self.imagenCheckbox = QPixmap("imagenes/checkBoxEstadoPedido.PNG")
        self.checkboxEstadoPedido.setPixmap(self.imagenCheckbox)

        # agregamos el label y el checkbox a formularioLayout
        self.formularioLayout.addRow(self.estadoPedido, self.checkboxEstadoPedido)

        # boton actualizar
        self.botonActualizar = QPushButton("Actualizar")
        self.botonActualizar.setStyleSheet("background-color: #f9b966; color: #000000; border-radius: 10px; margin-left: 10px")






        self.botonActualizar.setFixedSize(200, 30)
        self.botonActualizar.setFont(QFont("Arial", 15))
        # boton eliminar
        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setFixedSize(200, 30)
        self.botonEliminar.setStyleSheet("background-color: #f9b966; color: #000000; border-radius: 10px; margin-left: 50px")
        self.botonEliminar.setFont(QFont("Arial", 15))

        # agregamos los botones actualizar y eliminar a formularoLayout
        self.formularioLayout.addRow(self.botonActualizar, self.botonEliminar)





        # agregamos el formulario a el horizontalTablaYFormulario
        self.horizontalTablaYFormulario.addWidget(self.formularioEditarPedido)




        # agregamos el widget tablaYFormulario a la vertical principal
        self.verticalPrincipal.addWidget(self.tablaYFormulario)



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