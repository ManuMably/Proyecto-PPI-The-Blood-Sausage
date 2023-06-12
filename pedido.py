class Pedido:

    def __init__(self, nombreCliente,
                 direccion,
                 celular,
                 morcillaCantidad,
                 chorizoCantidad,
                 arrozCantidad,
                 estadoPedido):

        self.nombreCliente = nombreCliente
        self.direccion = direccion
        self.celular = celular
        self.morcillaCantidad = morcillaCantidad
        self.chorizoCantidad = chorizoCantidad
        self.arrozCantidad = arrozCantidad
        self.estadoPedido = estadoPedido

    def __str__(self):
        return f"Nombre Cliente: {self.nombreCliente} Direccion: {self.direccion} Celular: {self.celular} CantidadMoricilla: {self.morcillaCantidad} CantidadChorizo: {self.chorizoCantidad} CantidadArroz: {self.arrozCantidad} EstadoPedido: {self.estadoPedido}"
