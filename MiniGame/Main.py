#Crear sistema de 2 Turnos
import os
from turtle import pos
from Modelo.Personaje import *

Turno = 1

P1 = Personaje("Player 1")
P2 = Personaje("Player 2")


while True:
    os.system("cls")
    print(f"Turno Actual: {Turno}\n")

    #Stats
    print(f"Stats Player 1:\nVida:{P1.getVida()}\nFuerza: {P1.getFuerza()}\nOro: {P1.getOro()}\n")
    print(f"Stats Player 2:\nVida: {P2.getVida()}\nFuerza: {P2.getFuerza()}\nOro: {P2.getOro()}\n")


    print("Opciones: \n")
    print("[1] - Atacar\n")
    print("[2] - Comprar\n")

    opcion = input("Selecciona tu Jugada: ")

    if opcion == "1":

        if Turno == 1: P1.Atacar(P2)
        else: P2.Atacar(P1)

    if opcion == "2":
        os.system("cls")
        from Tienda import *
        position = 1
        for item in Tiendita:
            print(f"[{position}] - [Coste: {item.getCoste()}]{item.getNombre()}[Vida:{item.getVida()}][Fuerza:{item.getFuerza()}]")
            position += 1
        seleccion = int(input("Selecciona el N° del item que quieres comprar: "))

        if Turno == 1: P1.Comprar(Tiendita[seleccion - 1])
        else: P2.Comprar(Tiendita[seleccion - 1])

        print("Item Comprado. Presiona Enter para Continuar!")









    input("Turno Terminado. Presione Enter para Continuar!")
    if Turno==1: Turno = 2
    else: Turno = 1

    


