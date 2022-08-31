#Identificar y generar los modelos de clases para crear un sistema que administre un taller mecanico.
#Es decir, las reparaciones que en este se generan, los repuestos que se utilizan, los autos que ingresan 
#los mecanicos que hacen las reparaciones y los clientes a los que se atienden.

class cliente:
    rut = None
    nombres = None
    apellidos = None

class Auto:
    patente = None
    dueño = ""


C1 = cliente()
C1.rut = "11.111.111-1"
C1.apellidos = "Sanchez"
C1.nombres = "Alexis"

A1 = Auto()
A1.patente = "FSSS34"
A1.dueño = C1

print(A1.dueño.rut)

C1.nombres = "Arturo"

print(A1.dueño.nombres)