import mysql.connector
from mysql.connector import errorcode

class DAO:
    #Data Access Object
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root', 
                password='',
                host='localhost',
                database='DBPOOIEIV')
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


    def EliminarItem(self, ItemId):
        cursor = self.cnx.cursor()
        consulta = ("DELETE FROM Items WHERE ItemId = %s")
        data = (ItemId,)
        cursor.execute(consulta, data)
        self.cnx.commit()

    def ActualizarItem(self, Item):
        cursor = self.cnx.cursor()
        upt_item = ("UPDATE Items SET Nombre = %s, Vida = %s, Fuerza = %s, Armadura = %s, Coste = %s WHERE ItemID = %s")
        data_item = (Item.getNombre(), Item.getVida(), Item.getFuerza(), Item.getArmadura(), Item.getCoste(), Item.getItemId())
        cursor.execute(upt_item, data_item)
        self.cnx.commit()