import mysql.connector
from mysql.connector import errorcode

class DAO:
    #Data Access Object
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user='sql10549760', 
                password='n4AtcPLJrd',
                host='sql10.freemysqlhosting.net',
                database='sql10549760')
            print("Coneccion Establecida")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de Usuario o Contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de Datos no Existe")
            else:
                print(err)

    def InsertarItem(self, Item):
        addItem = ("INSERT INTO Items (Nombre, Vida, Fuerza, Armadura, Coste)"
                "VALUES (%s, %s, %s, %s, %s)")

        dataItem = (Item.getNombre(), Item.getVida(), Item.getFuerza(), Item.getArmadura(), Item.getCoste())

        cursor = self.cnx.cursor()
        cursor.execute(addItem, dataItem)
        self.cnx.commit()
        cursor.close()
        #self.cnx.close()

    def LeerItems(self):
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * FROM Items")

        listaItems = []

        for(ItemId, Nombre, Vida, Fuerza, Coste, Armadura) in cursor:
            from Model.Item import Item
            i = Item(ItemId, Nombre, Vida, Fuerza, Coste, Armadura)
            listaItems.append(i)
        
        return listaItems