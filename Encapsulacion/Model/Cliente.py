class Cliente:
    
    def __init__(self, rut, nombres, apellidos):
        self.__Rut = rut
        self.__Nombres = nombres
        self.__Apellidos = apellidos

    def getRut(self):
        return self.__Rut
    
    def setRut(self, nuevoRut):
        self.__Rut = nuevoRut

    def getNombre(self):
        return f"{self.__Nombres} {self.__Apellidos}"