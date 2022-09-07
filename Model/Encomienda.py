from posixpath import split
from Cliente import *
import datetime
class Encomienda:
    id = None
    fecha = None
    remitente = None
    destinatario = None
    observacion = ""

    def __init__(self, id, fecha, rem, des, obs):
        try:
            if not isinstance(id, int):
                raise TypeError("Id debe ser un entero.")
            if not (isinstance(rem, Cliente) and isinstance(des, Cliente)):
                raise TypeError("Remitente/Destinatario debe ser un Cliente.")
        except:
            print("Un Error ha ocurrido!")
        
        self.id = id # Entero
        self.fecha = fecha
        self.remitente = rem
        self.destinatario = des
        self.observacion = str(obs).upper() # sdsAAAAcsds

    def getInfo(self):
        return f"N° Encomienda: {self.id}, Fecha: {self.fecha}, Remitente: {self.remitente}, Destinatario: {self.destinatario}"
        #return "N° Encomienda:"N° Encomienda: " + self.id + ", Fecha: " + self.fecha + ", Remitente: " + self.remitente + ", Destinatario: " + self.destinatario + " + self.id + ", Fecha: " + self.fecha + ", Remitente: " + self.remitente + ", Destinatario: " + self.destinatario + ""

class Persona:
    rut = ""
    nombres = ""
    apellidos =""

    def __init__(self, rut, nom, ape):
        self.rut = "1.111.111-1"


        lista = str(nom).split(" ")
        newName = ""
        for val in lista:
            newName += val.capitalize() + " "
        newApe = ""
        lista = str(ape).split(" ")
        for val in lista:
            newApe += val.capitalize() + " "
        self.nombres = newName# ALEXIS ARTURO
        self.apellidos = newApe # Riquelme Andrade


P = Persona("1.111.111-1", "ALEXIS ARTURO", "riQUElme anDRAde")
print(P.nombres + " " + P.apellidos)


C1 = Cliente("1-1", "A", "B")

E1 = Encomienda(1, datetime.datetime.now(), C1, C1, "Encomienda 1")

