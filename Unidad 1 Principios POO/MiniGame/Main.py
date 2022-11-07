#Crear sistema de 2 Turnos
import os
from Modelo.Personaje import *

Turno = 1

P1 = Personaje("Player 1")
P2 = Personaje("Player 2")

Ganador = None

while True:
    os.system("cls")
    print(f"Turno Actual: {Turno}\n")

    #Stats
    print(f"Stats Player 1:\nVida:{P1.getVida()}\nFuerza: {P1.getFuerza()}\nOro: {P1.getOro()}\n")
    print(f"Inventario P1: {P1.obtenerInventario()}\n")
    
    
    print(f"Stats Player 2:\nVida: {P2.getVida()}\nFuerza: {P2.getFuerza()}\nOro: {P2.getOro()}\n")
    print(f"Inventario P2: {P2.obtenerInventario()}\n")

    print("Opciones: \n")
    print("[1] - Atacar")
    print("[2] - Comprar")
    print("[3] - Vender")

    opcion = input("Selecciona tu Jugada: ")

    if opcion == "1":

        if Turno == 1: 
            P1.Atacar(P2)
            if P2.getVida() <= 0:
                Ganador = P1
        else: 
            P2.Atacar(P1)
            if P1.getVida() <= 0:
                Ganador = P2

        if Ganador != None:
            break

    if opcion == "2":
        os.system("cls")
        from Tienda import *
        position = 1
        for item in Tiendita:
            print(f"[{position}] - [Coste: {item.getCoste()}]{item.getNombre()}[Vida:{item.getVida()}][Fuerza:{item.getFuerza()}]")
            position += 1
        seleccion = int(input("Selecciona el N° del item que quieres comprar: "))

        if Turno == 1: 
            print(P1.Comprar(Tiendita[seleccion - 1]))
        else: 
            print(P2.Comprar(Tiendita[seleccion - 1]))

        #print("Item Comprado. Presiona Enter para Continuar!")

    if opcion == "3":
        if Turno == 1:
            #Vende P1
            os.system("cls")
            indice = 1
            for i in P1.getInventario():
                print(f"{indice} - {i.getNombre()}")
                indice += 1

            opcion = int(input("Selecciona el Item a Vender: "))
            P1.Vender(P1.getInventario()[opcion - 1])
        else:
            #Vende 2
            os.system("cls")
            indice = 1
            for i in P2.getInventario():
                print(f"{indice} - {i.getNombre()}")
                indice += 1

            opcion = int(input("Selecciona el Item a Vender: "))
            P2.Vender(P2.getInventario()[opcion - 1])

        print("Item Vendido")



















    input("Turno Terminado. Presione Enter para Continuar!")
    if Turno==1: Turno = 2
    else: Turno = 1

print(f"Player {Ganador.getNombre()} gana la Partida!!!")
input("")  


