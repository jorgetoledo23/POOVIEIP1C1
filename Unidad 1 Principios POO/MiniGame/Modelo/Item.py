class Item:

    def __init__(self, nombre:str, vida:int, fuerza:int, coste:int):
        self.__Nombre = nombre
        self.__Vida = vida
        self.__Fuerza = fuerza
        self.__Coste = coste
    
    def getNombre(self):
        return self.__Nombre

    def getVida(self):
        return self.__Vida
    
    def getFuerza(self):
        return self.__Fuerza

    def getCoste(self):
        return self.__Coste