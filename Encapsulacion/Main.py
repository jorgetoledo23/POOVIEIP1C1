from Model.Cliente import *
from Model.Encomienda import *

c = Cliente("1-1", "Aaa Aaa", "Bbb Bbb")
print(c.getRut())
#c.__Rut = "2-2"
c.setRut("2-2")
print(c.getRut())

print(c.getNombre())
c.Edad = 10

print(c.Edad)

