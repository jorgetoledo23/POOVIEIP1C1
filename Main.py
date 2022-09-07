from Model.Cliente import *
from Model.Encomienda import *
import datetime

while (True):

    print("Sistema de Encomiendas")

    print("[1]-Ingresar Nuevo Cliente")
    print("[2]-Ingresar Encomienda")
    print("[3]-Listar Clientes")
    print("[4]-Listar Encomiendas")
    
    opcion = input("Selecciona la Opcion: ")

    if(opcion == "1"):
        #Ingreso de Cliente
        rutCliente = input("Ingrese Rut: ")
        nom = input("Ingrese Nombres: ")
        ape = input("Ingrese Apellidos: ")
        C1 = Cliente(rutCliente, nom, ape) #Crear Objeto => Instancia
        #BD
        listaClientes.append(C1)
        input(f"Cliente {C1.getInfo()} creado Exitosamente!")

    if(opcion == "2"):
        id = len(listaEncomiendas) + 1
        fecha = datetime.datetime.now() #import datetime
        remitente = input("Ingrese Rut Remitente: ")
        destinatario = input("Ingrese Rut Destinatario: ")
        
        Enc = Encomienda(id, fecha, remitente, destinatario)
        listaEncomiendas.append(Enc)
        input(f"Encomienda {Enc.getInfo()} creada Exitosamente!")

    if(opcion == "3"):
        for cliente in listaClientes:
            print(f"{cliente.getInfo()}")
            print("------------------")
        input("Clientes Listados. Presiona para continuar!")

    if(opcion == "4"):
        for encomienda in listaEncomiendas:
            print(f"{encomienda.getInfo()}")
            print("------------------")
        input("Encomiendas Listadas. Presiona para continuar!")