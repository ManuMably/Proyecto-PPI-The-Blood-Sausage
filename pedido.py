class Pedido:

    def __init__(self, nombreCliente,
                 celular,
                 direccion,
                 morcillaCantidad,
                 chorizoCantidad,
                 arrozCantidad,
                 estadoPedido):

        self.nombreCliente = nombreCliente
        self.celular = celular
        self.direccion = direccion
        self.morcillaCantidad = morcillaCantidad
        self.chorizoCantidad = chorizoCantidad
        self.arrozCantidad = arrozCantidad
        self.estadoPedido = estadoPedido