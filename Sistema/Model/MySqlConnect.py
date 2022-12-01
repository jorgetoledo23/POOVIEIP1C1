import mysql.connector
from mysql.connector import errorcode
from Model.Cliente import Cliente
from Model.Producto import Producto
from Model.Venta import Venta
from Model.DetalleVenta import DetalleVenta

class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root', 
                password='root',
                host='localhost',
                database='VentasPython')
            print("Coneccion Establecida")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de Usuario o Contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de Datos no Existe")
            else:
                print(err)


    def LeerClientes(self):
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * FROM Clientes")
        listaClientes = []
        for(a, b, c, d) in cursor:
            objetoTipoCliente = Cliente(a,b,c,d)
            listaClientes.append(objetoTipoCliente)
        return listaClientes
    
    def LeerProductos(self):
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * FROM Productos")
        listaProductos = []
        for(a, b, c, d) in cursor:
            objetoTipoProducto = Producto(a,b,c,d)
            listaProductos.append(objetoTipoProducto)
        return listaProductos

    def LeerVentas(self):
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * FROM Ventas")
        listaVentas = []
        for(a, b, c, d) in cursor:
            objetoTipoVenta = Venta(a,b,c,d)
            listaVentas.append(objetoTipoVenta)
        return listaVentas

    def LeerDetalleVenta(self, codigoVenta):
        cursor = self.cnx.cursor(buffered=True)
        query = ("SELECT * FROM detalleventa WHERE ventaid = %s")
        data = (codigoVenta,)
        cursor.execute(query, data)
        listaDetalle = []
        for(a, b, c, d, e) in cursor:
            producto = self.LeerProductoById(c)
            objetoTipoDetalle = DetalleVenta(a,b,producto,d,e)
            listaDetalle.append(objetoTipoDetalle)
        return listaDetalle

    def LeerProductoById(self, codigoProduto):
        cursor = self.cnx.cursor(buffered=True)
        query = ("SELECT * FROM Productos WHERE productoid = %s")
        data = (codigoProduto,)
        cursor.execute(query, data)
        for(a, b, c, d) in cursor:
            objetoTipoDetalle = Producto(a,b,c,d)
        return objetoTipoDetalle
    

    def InsertarVenta(self, rutCliente, total, fecha, detalle):
        try:
            cursor = self.cnx.cursor()
            addVenta = ("INSERT INTO ventas (rutcliente, fecha, totalventa) values (%s, %s, %s)")
            dataVenta = (rutCliente, fecha, total)
            cursor.execute(addVenta, dataVenta)
            ventaid = cursor.lastrowid
            for dv in detalle:
                addDetalle = ("INSERT INTO detalleventa (ventaid, productoid, cantidad, subtotal) values (%s, %s, %s ,%s)")
                dataDetalle = (ventaid, dv.getProducto().getCodigo(), dv.getCantidad(), dv.getSubtotal())
                cursor.execute(addDetalle, dataDetalle)
                
                #Descontar Stock (Update)
            
            self.cnx.commit()
        except:
            self.cnx.rollback()