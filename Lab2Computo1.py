
inventario = [
    ["ID001", "Tomate", 50],
    ["ID002", "Queso", 20],
    ["ID003", "Frijoles", 20]
]

ventas = []

empleados = []


def crear_factura():
    print("\n********** CREAR FACTURA **********")

    ncliente = input("Ingrese el nombre del cliente: ")
    nprod = input("Ingrese el nombre del producto: ")

    punitario = float(input("Ingrese el precio unitario: "))
    prodcantidad = int(input("Ingrese la cantidad del producto: "))

    subtotal = punitario * prodcantidad
    desc = input("¿El producto posee descuento? (s/n): ").strip().lower()
    descuento = 0

    if desc == "s":
        descuento = float(input("Ingrese el descuento: "))
        if descuento > subtotal:
            descuento = subtotal

    subtotal_descuento = subtotal - descuento
    prop = input("¿Desea agregar propina? (s/n): ").strip().lower()
    propina = 0

    if prop == "s":
        propina = float(input("Ingrese la propina: "))
    total = subtotal_descuento + propina

    print("\n************************************")
    print("           FACTURA FINAL")
    print("************************************")
    print(f"Nombre del cliente : {ncliente}")
    print(f"Producto           : {nprod}")
    print(f"Precio unitario    : ${punitario}")
    print(f"Cantidad           : {prodcantidad}")
    print(f"Subtotal           : ${subtotal}")
    print(f"Descuento          : ${descuento}")
    print(f"Subtotal con desc. : ${subtotal_descuento}")
    print(f"Propina            : ${propina}")
    print("------------------------------------")
    print(f"TOTAL FINAL        : ${total}")
    print("************************************")

# PARTE 2 INVENTARIO


def mostrar_inventario():
    print("\n******** INVENTARIO ********")

    for producto in inventario:
        print(
            f"ID: {producto[0]} | "
            f"Producto: {producto[1]} | "
            f"Cantidad: {producto[2]}"
        )


def retirar_inventario():
    print("\n******** RETIRAR INGREDIENTES *******")

    mostrar_inventario()
    retiros = []

    while True:

        id_producto = input(
            "\nIngrese el ID del ingrediente que desea retirar "
            "(0 para terminar): "
        ).strip()

        if id_producto == "0":
            break
        encontrado = False
        for producto in inventario:

            if producto[0] == id_producto:

                encontrado = True

                cantidad = int(
                    input(
                        f"Ingrese la cantidad de {producto[1]} "
                        f"que desea retirar: "
                    )
                )

                # Comprobar que exista suficiente inventario
                if cantidad <= producto[2] and cantidad > 0:

                    retiros.append(
                        [producto[0], producto[1], cantidad]
                    )

                    print(
                        f"Se agregaron {cantidad} unidades de "
                        f"{producto[1]} al retiro."
                    )

                elif cantidad > producto[2]:

                    print(
                        f"ERROR: No hay suficiente {producto[1]} "
                        f"en el inventario."
                    )

                else:

                    print("La cantidad debe ser mayor que 0.")

                break
        if not encontrado:
            print("ERROR: El ID del producto no existe.")
    if len(retiros) > 0:

        puede_retirar = True

        for retiro in retiros:

            for producto in inventario:

                if producto[0] == retiro[0]:

                    if retiro[2] > producto[2]:
                        puede_retirar = False

        if puede_retirar:

            # Realizar los retiros
            for retiro in retiros:

                for producto in inventario:

                    if producto[0] == retiro[0]:

                        producto[2] -= retiro[2]

            print("\nRetiro realizado correctamente.")

            print("\n******** REPORTE DE INVENTARIO *******")

            mostrar_inventario()

        else:

            print(
                "\nNo se realizó el retiro porque "
                "uno o más ingredientes no tienen suficiente existencia."
            )

# PARTE 3 - PLATILLO MÁS VENDIDO


def registrar_ventas():

    print("\n******** REGISTRAR VENTAS ********")

    while True:

        platillo = input(
            "Ingrese el nombre del platillo vendido "
            "(0 para terminar): "
        ).strip()

        if platillo == "0":
            break

        cantidad = int(
            input("Ingrese la cantidad vendida: ")
        )

        if cantidad > 0:

            ventas.append(
                [platillo, cantidad]
            )

            print("Venta registrada correctamente.")

        else:

            print("La cantidad debe ser mayor que 0.")

    print("\n******** REPORTE DE VENTAS ********")

    if len(ventas) == 0:

        print("No existen ventas registradas.")
        return

    for venta in ventas:

        print(
            f"Platillo: {venta[0]} | "
            f"Cantidad vendida: {venta[1]}"
        )

    # Buscar el platillo más vendido
    mayor = 0
    platillo_mayor = ""

    for venta in ventas:

        if venta[1] > mayor:

            mayor = venta[1]
            platillo_mayor = venta[0]

    print("----------------------------------------")
    print(
        f"PLATILLO MÁS VENDIDO: {platillo_mayor}"
    )
    print(
        f"CANTIDAD VENDIDA: {mayor}"
    )


# PARTE 4 - EMPLEADOS

class Empleado:

    def __init__( self,nombre,edad,meses_trabajados,salario_base):

        self.nombre = nombre
        self.edad = edad
        self.meses_trabajados = meses_trabajados
        self.salario_base = salario_base

    def calcular_salario(self):

        años = self.meses_trabajados // 12
        salario = self.salario_base * (1.10 ** años)

        return salario

    def mostrar_informacion(self):

        print("\n------------------------------------")
        print("INFORMACIÓN DEL EMPLEADO")
        print("------------------------------------")
        print(f"Nombre           : {self.nombre}")
        print(f"Edad             : {self.edad}")
        print(f"Meses trabajados : {self.meses_trabajados}")
        print(f"Salario base     : ${self.salario_base:.2f}")
        print(f"Salario actual   : ${self.calcular_salario():.2f}")


class Cocinero(Empleado):

    def __init__(
        self,
        nombre,
        edad,
        meses_trabajados,
        salario_base,
        especialidad
    ):

        super().__init__(
            nombre,
            edad,
            meses_trabajados,
            salario_base
        )

        self.especialidad = especialidad

    def mostrar_informacion(self):

        super().mostrar_informacion()

        print(f"Tipo de empleado : Cocinero")
        print(f"Especialidad     : {self.especialidad}")

class Mesero(Empleado):

    def __init__(self,nombre,edad,meses_trabajados,salario_base,turno):

        super().__init__(nombre,edad,meses_trabajados,salario_base
        )

        self.turno = turno

    def mostrar_informacion(self):

        super().mostrar_informacion()

        print(f"Tipo de empleado : Mesero")
        print(f"Turno            : {self.turno}")


def registrar_empleado():

    print("\n========== REGISTRAR EMPLEADO ==========")

    nombre = input("Nombre completo: ")
    edad = int(input("Edad: "))
    meses = int(input("Meses trabajados: "))
    salario = float(input("Salario base: "))

    print("\n1 - Cocinero")
    print("2 - Mesero")

    tipo = input("Seleccione el tipo de empleado: ")

    if tipo == "1":

        especialidad = input(
            "Ingrese la especialidad del cocinero: "
        )

        empleado = Cocinero(
            nombre,
            edad,
            meses,
            salario,
            especialidad
        )

        empleados.append(empleado)

        print("\nCocinero registrado correctamente.")

    elif tipo == "2":

        turno = input(
            "Ingrese el turno (matutino/vespertino): "
        )

        empleado = Mesero(
            nombre,
            edad,
            meses,
            salario,
            turno
        )

        empleados.append(empleado)

        print("\nMesero registrado correctamente.")

    else:

        print("Tipo de empleado no válido.")

def mostrar_empleados():

    print("\n========== EMPLEADOS ==========")

    if len(empleados) == 0:

        print("No existen empleados registrados.")

    else:

        for empleado in empleados:

            empleado.mostrar_informacion()




while True:

    print("\n========================================")
    print("       Que desea hacer?        ")
    print("========================================")
    print("1 - Crear una factura")
    print("2 - Retirar ingredientes del inventario")
    print("3 - Registrar platillos vendidos")
    print("4 - Registrar empleado")
    print("5 - Mostrar empleados")
    print("6 - Mostrar inventario")
    print("7 - Salir")
    print("========================================")

    opcion = input("¿Qué desea hacer?: ")

    if opcion == "1":
        crear_factura()
    elif opcion == "2":
        retirar_inventario()
    elif opcion == "3":
        registrar_ventas()
    elif opcion == "4":
        registrar_empleado()
    elif opcion == "5":
        mostrar_empleados()
    elif opcion == "6":
        mostrar_inventario()
    elif opcion == "7":
        print("\nPrograma finalizado.")
        break
    else:
        print("\nOpción no válida.")

#PREGUNTAS
                 
#1 Es importante verificar todos los ingredientes antes de descontar cualquiera porque, si uno no tiene
# suficiente cantidad, no se debe realizar la operación. Así se evita que el inventario quede incorrecto
# o con cantidades negativas.

#2 La herencia permite reutilizar atributos y métodos como nombre, edad, meses trabajados y salario y asi
# se evita repetir código. Si Hernán agrega otro tipo de empleado, puede crear otra clase que herede de Empleado.

# 3 El total sería mayor, porque la propina se calcularía sobre un subtotal más alto, antes de aplicar el descuento. 
# Al aplicar primero el descuento, la cantidad sobre la que se calcula la propina es menor.
        
        

            

