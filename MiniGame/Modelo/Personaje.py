class Personaje:
    def __init__(self, nombre):
        self.__Nombre = nombre
        self.__Vida = 100
        self.__Fuerza = 100
        self.__Oro = 1000
        self.__Inventario = []

    def getNombre(self):
        return self.__Nombre

    def getVida(self):
        return self.__Vida
    
    def getFuerza(self):
        return self.__Fuerza

    def getOro(self):
        return self.__Oro

    def setVida(self, vida):
        self.__Vida -= vida
        return self.__Vida
   
    def Atacar(self, Objetivo):
        valorGolpe = self.__Fuerza / 15 + 10
        Objetivo.setVida(valorGolpe)

    def Comprar(self, ItemComprado):
        self.__Oro -= ItemComprado.getCoste()
        self.__Vida += ItemComprado.getVida()
        self.__Fuerza += ItemComprado.getFuerza()
        self.__Inventario.append(ItemComprado)
