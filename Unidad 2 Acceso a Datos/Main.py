from Model.MySqlConnection import DAO

dao = DAO()

while True:

    import os
    os.system("cls")

    print("[1] - Gestionar Items")
    print("[2] - Gestionar Personajes\n")

    opcion = input("Selecciona Opcion: ")
    if opcion == "1":
        import os
        os.system("cls")

        print("[1] - Ver Listado Items")
        print("[2] - Crear Items")
        print("[3] - Editar Item")
        print("[4] - Eliminar Item\n")

        opcion = input("Selecciona Opcion: ")

        if opcion == "1":
            for item in dao.LeerItems():
                print(item.getStats())
            input("")

        if opcion == "2":
            nom = input("Ingrese Nombre del Item: ")
            vida = input("Ingrese Vida del Item: ")
            fuerza = input("Ingrese Fuerza del Item: ")
            arm = input("Ingrese Armadura del Item: ")
            coste = input("Ingrese Coste del Item: ")

            from Model.Item import Item
            i = Item(1, nom, int(vida), int(fuerza), int(arm), int(coste))
            dao.InsertarItem(i)
            input("Item Creado. Presiona Enter para Continuar!")