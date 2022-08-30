class Encomienda:
    id = None
    fecha = None
    remitente = None
    destinatario = None

    def __init__(self, id, fecha, rem, des):
        self.id = id
        self.fecha = fecha
        self.remitente = rem
        self.destinatario = des

    def getInfo(self):
        #return f"N° Encomienda: {self.id}, Fecha: {self.fecha}, Remitente: {self.remitente}, Destinatario: {self.destinatario}"
        return "N° Encomienda: " + self.id + ", Fecha: " + self.fecha + ", Remitente: " + self.remitente + ", Destinatario: " + self.destinatario + ""