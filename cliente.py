
class Cliente:

    def __init__(self, nombreCompleto,
                 direccion,
                 celular,):

        self.nombreCompleto = nombreCompleto
        self.direccion = direccion
        self.celular = celular

    def __str__(self):
        return f"Nombre: {self.nombreCompleto} Direccion: {self.direccion} Celular: {self.celular}"