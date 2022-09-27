class Personaje:
    def __init__(self, nombre):
        self.__Nombre = nombre
        self.__Vida = 100
        self.__Fuerza = 100
        self.__Oro = 100
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
        valorGolpe = int(self.__Fuerza / 15 + 10)
        Objetivo.setVida(valorGolpe)

    def Comprar(self, ItemComprado):
        if self.__Oro >= ItemComprado.getCoste():
            self.__Oro -= ItemComprado.getCoste()
            self.__Vida += ItemComprado.getVida()
            self.__Fuerza += ItemComprado.getFuerza()
            self.__Inventario.append(ItemComprado)
            return "Item Comprado."
        else:
            return "Saldo insuficiente!"

    def Vender(self, ItemVendido):
        self.__Oro += int(ItemVendido.getCoste() / 2)
        self.__Vida -= ItemVendido.getVida()
        self.__Fuerza -= ItemVendido.getFuerza()
        self.__Inventario.remove(ItemVendido)


    def obtenerInventario(self):
        inv = ""
        for i in self.__Inventario:
           inv += f"[{i.getNombre()}] - "
        return inv

    def getInventario(self):
        return self.__Inventario







