#Identificar y generar los modelos de clases para crear un sistema para administrar las atenciones medicas
#de una consulta.
#Es decir, controlar los medicos que trabajan, las horas medicas, a que pacientes atienden, y el detalle de cada consulta
#que realizan.

class Medico:
    rut = ""
    nombres =""
    apellidos =""
    direccion =""
    comuna =""
    telefono = ""
    correo =""
    especialidad = ""

class Paciente:
    rut = ""
    nombres =""
    apellidos =""
    direccion =""
    comuna =""
    telefono = ""
    correo =""

class HoraMedica:
    fecha = ""
    lugar = ""
    doctor = ""
    valor = ""

class Atencion:
    horaMedica = ""
    detalle = ""

class Examen:
    codigo = ""


