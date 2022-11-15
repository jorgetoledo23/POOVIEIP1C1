from Model.MySqlConnection import DAO
from Model.Item import Item
import os

Dao = DAO()

while True:


    os.system("cls")

    print("[1] - Gestionar Items")
    print("[2] - Gestionar Personajes\n")

    opcion = input("Selecciona Opcion: ")
    if opcion == "1":
        
        os.system("cls")

        print("[1] - Ver Listado Items")
        print("[2] - Crear Items")
        print("[3] - Editar Item")
        print("[4] - Eliminar Item\n")

        opcion = input("Selecciona Opcion: ")

        if opcion == "1":
            for item in Dao.LeerItems():
                print(item.getStats())
            input("\nItems desplegados! Presiona Enter para Continuar...")
                
        if opcion == "2":
            #Insertar Item
            os.system("cls")
            nom = input("Ingresa Nombre del Item: ")
            fuerza = input("Ingresa Fuerza del Item: ")
            vida = input("Ingresa Vida del Item: ")
            arm = input("Ingresa Armadura del Item: ")
            valor = input("Ingresa Coste del Item: ")
            I = Item(1, nom, vida, fuerza, arm, valor)
            Dao.InsertarItem(I)
            input("Item agregado exitosamente! Presiona Enter para Continuar...")
        
        if opcion == "4":
            id = input("Ingresa el Id del item que quiere Eliminar: ")
            try:
                Dao.EliminarItem(id)
                input("\nItem eliminado exitosamente! Presiona Enter para Continuar...")
            except:
                print("\nError al Eliminar")

        if opcion == "3":
            id = input("Ingresa el Id del item que quiere Actualizar: ")
            os.system("cls")
            nom = input("Ingresa Nombre del Item: ")
            fuerza = input("Ingresa Fuerza del Item: ")
            vida = input("Ingresa Vida del Item: ")
            arm = input("Ingresa Armadura del Item: ")
            valor = input("Ingresa Coste del Item: ")
            I = Item(id, nom, vida, fuerza, arm, valor)
            Dao.ActualizarItem(I)
            input("\nItem actualizado exitosamente! Presiona Enter para Continuar...")