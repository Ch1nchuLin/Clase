#Realizar un registro telefonico de celular
#El regstro pide lo siguinete obligtoriamente
#Nombre de la persona
#Nombre de telefono
#De manera opcionar puede guardarse el apellido
#Los campos obligatoriaos deben revisarse
#Que vayan completos al momento de ingresar los datos

Registro = [("Maria","Zardoya",77773563)]

print("*****************************")
print("*** [Registro Telefonico] ***")
print("*****************************\n")

while True:
    print("****Ingrese los datos telefonicos****\n")

    nombre = input("Ingrese el nombre: ")
    numero = int(input("Ingrese el numero telefonico: "))
    if nombre or numero == ():
        continue

    opcion = input("Desea agregar un apellido al registro")

    