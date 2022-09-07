class Encomienda:
    Id = None
    Remitente = None #Cliente
    Direccion = None

    def __init__(self, id, rem, dir):
        self.Id = id
        self.Remitente = rem
        self.Direccion = dir