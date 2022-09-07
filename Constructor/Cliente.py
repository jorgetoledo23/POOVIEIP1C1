class Cliente:
    #Atributos => Caracteristicas que lo definen
    id = None
    email = None
    telefono = None
    rut = None
    nombres = None
    apellidos = ""
    direccion = ""
    comuna = ""
    ciudad = ""

    #Metodos

    #Constructor
    def __init__(self, rut, nom, ape):
        self.rut = rut
        self.nombres = nom
        self.apellidos = ape


    def getInfo(self):
        return f"Rut: {self.rut}, Nombres: {self.nombres}, Apellidos: {self.apellidos}"

    def getInfoDetallada(self):
        pass
