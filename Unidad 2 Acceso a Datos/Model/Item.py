class Item:

    def __init__(self, Id:int, nombre:str, vida:int, fuerza:int, arm:int, coste:int):
        self.__ItemId = Id
        self.__Nombre = nombre
        self.__Vida = vida
        self.__Fuerza = fuerza
        self.__Coste = coste
        self.__Armadura = arm

    def getStats(self):
        return f"ItemId: [{self.__ItemId}] Coste: [{self.__Coste}] Nombre: [{self.__Nombre}] Vida: [{self.__Vida}] Fuerza: [{self.__Fuerza}] Armadura: [{self.__Armadura}]"
    def getItemId(self):
        return self.__ItemId
    def getCoste(self):
        return self.__Coste
    def getVida(self):
        return self.__Vida
    def getFuerza(self):
        return self.__Fuerza
    def getNombre(self):
        return self.__Nombre
    def getArmadura(self):
        return self.__Armadura