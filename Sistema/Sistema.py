from Model.MySqlConnect import DAO
import os
from datetime import datetime
from Model.DetalleVenta import DetalleVenta

dao = DAO()

while True:
    os.system("cls")
    print("[1] - Vender")
    print("[2] - Ver Historial de Ventas")

    opcion = input("\nSelecciona una Opcion: ")

    if(opcion == "1"):
        #Venta
        os.system("cls")
        carritoCompra = []
        Total = 0

        #Mostrar Listado Clientes
        for c in dao.LeerClientes():
            print(c.getInfo())

        existe = True
        while existe:
            rutCliente = input("\nIngresa Rut Cliente: ")
            for c in dao.LeerClientes():
                if(rutCliente == c.getRut()):
                   existe = False 
                   cliente = c
            if(existe):
                #Rut Invalido
                input("Rut Invalido. Intenta de nuevo...")

        agregando = True
        while agregando:
            os.system("cls")
            print(f"Venta para Cliente: {cliente.getInfo()}")
            print(f"Fecha: {datetime.now().date()}\n")

            print("Producto Disponibles para la Venta\n")
            for p in dao.LeerProductos():
                print(p.getInfo())

            existe = True
            while existe:
                codigoProducto = int(input("\nIngresa Codigo del Producto a Vender: "))#
                for p in dao.LeerProductos():
                    if(codigoProducto == p.getCodigo()):
                        existe = False 
                        producto = p
                if(existe):
                    #Producto Invalido
                    input("Producto Invalido. Intenta de nuevo...")


            cantidad = int(input("\nCantidad Deseada?: "))

            dv = DetalleVenta(1,1,producto,cantidad, producto.getPrecio() * cantidad)
            carritoCompra.append(dv)
            #Aumentar Total
            Total += producto.getPrecio() * cantidad

            respuesta = input("Producto Agregado a la Venta. Desea agregar mas Productos? (S/N): ")
            if(respuesta != "s" and respuesta != ("S")):
                agregando = False
        
        #Resumen Venta
        os.system("cls")
        print(f"Venta para Cliente: {cliente.getInfo()}")
        print(f"Fecha: {datetime.now().date()}\n")

        print("Detalle Venta")

        for dv in carritoCompra:
            print(dv.getShortInfo())

        print(f"\nTotal Venta: {Total}")

        input("Presione Enter para Confirmar la Venta!")
        dao.InsertarVenta(rutCliente, Total, datetime.now().date(), carritoCompra)

    if(opcion == "2"):
        os.system("cls")
        print("Historial de Ventas\n")

        for v in dao.LeerVentas():
            print(v.getInfo())

        codigoventa = input("\nIngresa el Codigo de la Venta para ver su Detalle: ")

        os.system("cls")
        print("Detalle Venta: \n")
        for dv in dao.LeerDetalleVenta(codigoventa):
            print(dv.getShortInfo())

        input("")