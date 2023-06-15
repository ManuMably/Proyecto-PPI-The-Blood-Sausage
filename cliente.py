
class Cliente:

    def __init__(self,
                 cedula,
                 nombreCompleto,
                 direccion,
                 celular,):

        self.cedula = cedula
        self.nombreCompleto = nombreCompleto
        self.direccion = direccion
        self.celular = celular

    def __str__(self):
        return f"Nombre: {self.nombreCompleto} Cedula: {self.cedula}"
