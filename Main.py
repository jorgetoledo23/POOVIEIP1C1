from Model.Cliente import *

listaClientes = []

while (True):

    print("Sistema de Encomiendas")

    print("[1]-Ingresar Nuevo Cliente")
    print("[2]-Ingresar Encomienda")
    print("[3]-Listar Clientes")
    
    opcion = input("Selecciona la Opcion: ")

    if(opcion == "1"):
        #Ingreso de Cliente
        rutCliente = input("Ingrese Rut: ")
        nom = input("Ingrese Nombres: ")
        ape = input("Ingrese Apellidos: ")
        C1 = Cliente(rutCliente, nom, ape) #Crear Objeto => Instancia
        #BD
        listaClientes.append(C1)
        input(f"Cliente {C1.getInfo()}, Creado Exitosamente!")

    if(opcion == "2"):
        pass

    if(opcion == "3"):
        for cliente in listaClientes:
            print(f"{cliente.getInfo()}")
            print("------------------")
        input("Clientes Listados. Presiona para continuar!")