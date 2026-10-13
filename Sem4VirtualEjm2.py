class Persona():
    peso =''
    altura = ''
    sexo = ''
    nombre = ''
    puesto = '0' 
    salario = ''


class empleado(Persona):
    #Incluye nombre, puesto, trabajo
    nombre = ''
    puesto = ''
    salario = 0
    fechain = ''

    #Metodo constructor 
    def __init__(self,nombre,puesto,salario,fechain):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
        self.fechain = fechain
        
    #Acciones de el trabajador: Marcar, hacer reporte, declarar renta
    def marcaryasl(self,hora,tipo):
        hentrada = time(7,0,0)
        hsalida = time(4,0,0)

        if(tipo == "entrada" and hora>hentrada):
            return(f"Llegaste tarde {self.nombre}")
        else:
            return(f"Llegaste a tiempo {self.nombre}")