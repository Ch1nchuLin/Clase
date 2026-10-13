
# SISTEMA DE GESTIÓN PARA UN GIMNASIO

# CLASE PADRE: Persona

class Persona:

    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre         
        self.edad = edad             
        self.telefono = telefono      

    def mostrar_informacion(self):
        print("\n--- Información personal ---")
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Teléfono:", self.telefono)

    def cumplir_años(self):
        self.edad += 1
        print(self.nombre, "ahora tiene", self.edad, "años.")

# CLASE HIJA: Miembro

class Miembro(Persona):

    def __init__(self, nombre, edad, telefono, membresia, peso):
        super().__init__(nombre, edad, telefono)

        self.membresia = membresia    # str
        self.peso = peso              # float
        self.activo = True            # bool

    # Método 1
    def mostrar_informacion(self):
        print("\n--- Información del miembro ---")
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Teléfono:", self.telefono)
        print("Membresía:", self.membresia)
        print("Peso:", self.peso, "kg")
        print("Estado:", "Activo" if self.activo else "Inactivo")

    # Método 2
    def cambiar_estado(self):
        self.activo = not self.activo

        if self.activo:
            print("El miembro ahora está activo.")
        else:
            print("El miembro ahora está inactivo.")

    # Método adicional
    def calcular_pago(self, descuento=0):
        precios = {
            "basica": 20.0,
            "estandar": 30.0,
            "premium": 45.0
        }

        precio = precios.get(self.membresia.lower(), 0)

        pago = precio - (precio * descuento / 100)

        return pago


# ------------------------------------------------------------
# FUNCIONES EXTERNAS PARA LA CLASE PERSONA
# ------------------------------------------------------------

def mostrar_persona(persona):
    print("\nInformación desde función externa:")
    print("Nombre:", persona.nombre)
    print("Edad:", persona.edad)
    print("Teléfono:", persona.telefono)


def actualizar_edad(persona, cantidad=1):
    persona.edad += cantidad
    print("Edad actualizada:", persona.edad)


# ------------------------------------------------------------
# FUNCIONES EXTERNAS PARA LA CLASE MIEMBRO
# ------------------------------------------------------------

def mostrar_miembro(miembro):
    print("\nInformación del miembro desde función externa:")
    miembro.mostrar_informacion()


def calcular_membresia(miembro, descuento=0):
    pago = miembro.calcular_pago(descuento)

    if pago == 0:
        print("Tipo de membresía no válido.")
    else:
        print("Costo de la membresía: $", pago)


# ------------------------------------------------------------
# LISTA PARA AGRUPAR LOS DATOS
# ------------------------------------------------------------

miembros = []


# ------------------------------------------------------------
# REGISTRAR MIEMBRO
# ------------------------------------------------------------

def registrar_miembro():

    print("\n========== REGISTRO DE MIEMBRO ==========")

    try:
        nombre = input("Ingrese el nombre: ")

        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")

        edad = int(input("Ingrese la edad: "))

        if edad <= 0:
            raise ValueError("La edad debe ser mayor que 0.")

        telefono = input("Ingrese el teléfono: ")

        peso = float(input("Ingrese el peso en kg: "))

        if peso <= 0:
            raise ValueError("El peso debe ser mayor que 0.")

        print("\nTipos de membresía:")
        print("1. Básica - $20")
        print("2. Estándar - $30")
        print("3. Premium - $45")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            membresia = "basica"
        elif opcion == "2":
            membresia = "estandar"
        elif opcion == "3":
            membresia = "premium"
        else:
            raise ValueError("Tipo de membresía inválido.")

        nuevo_miembro = Miembro(
            nombre,
            edad,
            telefono,
            membresia,
            peso
        )

        miembros.append(nuevo_miembro)

        print("\n¡Miembro registrado correctamente!")

    except ValueError as error:
        print("Error:", error)

    except Exception as error:
        print("Ocurrió un error inesperado:", error)


# ------------------------------------------------------------
# MOSTRAR MIEMBROS
# ------------------------------------------------------------

def mostrar_miembros():

    if len(miembros) == 0:
        print("\nNo hay miembros registrados.")
        return

    print("\n========== MIEMBROS REGISTRADOS ==========")

    for i, miembro in enumerate(miembros, start=1):
        print("\nMiembro #", i)
        miembro.mostrar_informacion()


# ------------------------------------------------------------
# BUSCAR MIEMBRO
# ------------------------------------------------------------

def buscar_miembro():

    if len(miembros) == 0:
        print("\nNo hay miembros registrados.")
        return

    nombre = input("\nIngrese el nombre que desea buscar: ")

    encontrado = False

    for miembro in miembros:

        if miembro.nombre.lower() == nombre.lower():
            miembro.mostrar_informacion()
            encontrado = True
            break

    if not encontrado:
        print("No se encontró ningún miembro con ese nombre.")


# ------------------------------------------------------------
# CAMBIAR ESTADO DEL MIEMBRO
# ------------------------------------------------------------

def cambiar_estado_miembro():

    if len(miembros) == 0:
        print("\nNo hay miembros registrados.")
        return

    try:

        mostrar_miembros()

        numero = int(input("\nSeleccione el número del miembro: "))

        if numero < 1 or numero > len(miembros):
            raise ValueError("Número de miembro inválido.")

        miembro = miembros[numero - 1]

        miembro.cambiar_estado()

    except ValueError as error:
        print("Error:", error)


# ------------------------------------------------------------
# CALCULAR PAGO
# ------------------------------------------------------------

def calcular_pago_miembro():

    if len(miembros) == 0:
        print("\nNo hay miembros registrados.")
        return

    try:

        mostrar_miembros()

        numero = int(input("\nSeleccione el número del miembro: "))

        if numero < 1 or numero > len(miembros):
            raise ValueError("Número de miembro inválido.")

        miembro = miembros[numero - 1]

        respuesta = input(
            "¿Desea aplicar un descuento? (s/n): "
        ).lower()

        if respuesta == "s":

            descuento = float(
                input("Ingrese el porcentaje de descuento: ")
            )

            if descuento < 0 or descuento > 100:
                raise ValueError(
                    "El descuento debe estar entre 0 y 100."
                )

            calcular_membresia(miembro, descuento)

        else:

            calcular_membresia(miembro)

    except ValueError as error:
        print("Error:", error)


# ------------------------------------------------------------
# MENÚ PRINCIPAL
# ------------------------------------------------------------

def menu():

    while True:

        print("\n")
        print("==========================================")
        print("       SISTEMA DE GESTIÓN DEL GIMNASIO")
        print("==========================================")
        print("1. Registrar miembro")
        print("2. Mostrar miembros")
        print("3. Buscar miembro")
        print("4. Cambiar estado de miembro")
        print("5. Calcular pago de membresía")
        print("6. Salir")
        print("==========================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_miembro()

        elif opcion == "2":
            mostrar_miembros()

        elif opcion == "3":
            buscar_miembro()

        elif opcion == "4":
            cambiar_estado_miembro()

        elif opcion == "5":
            calcular_pago_miembro()

        elif opcion == "6":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nError: opción no válida.")


# ------------------------------------------------------------
# EJECUCIÓN DEL PROGRAMA
# ------------------------------------------------------------

menu()


# ============================================================
# DESCRIPCIÓN DEL SISTEMA
# ============================================================
#
# Este sistema permite administrar los miembros de un gimnasio,
# registrando sus datos personales, peso y tipo de membresía.
# También permite consultar miembros, cambiar su estado y
# calcular el costo de su membresía aplicando descuentos.
#
# ENTIDADES / CLASES:
#
# 1. Persona:
#    Representa los datos generales de una persona.
#
# 2. Miembro:
#    Representa a un cliente del gimnasio y hereda de Persona.
#
# DESCRIPCIÓN DE LAS CLASES:
#
# Clase Persona:
# Atributos:
# - nombre: nombre de la persona.
# - edad: edad de la persona.
# - telefono: número telefónico.
#
# Métodos:
# - mostrar_informacion(): muestra los datos de la persona.
# - cumplir_anios(): aumenta la edad de la persona.
#
# Clase Miembro:
# Hereda los atributos y métodos de Persona.
#
# Atributos:
# - membresia: tipo de membresía contratada.
# - peso: peso del miembro en kilogramos.
# - activo: indica si la membresía está activa.
#
# Métodos:
# - mostrar_informacion(): muestra los datos completos del miembro.
# - cambiar_estado(): cambia entre activo e inactivo.
# - calcular_pago(): calcula el precio de la membresía
#   y permite aplicar un descuento.
#
# FUNCIONES EXTERNAS:
#
# Para Persona:
# - mostrar_persona(): muestra información de una persona.
# - actualizar_edad(): actualiza la edad de una persona.
#
# Para Miembro:
# - mostrar_miembro(): muestra la información de un miembro.
# - calcular_membresia(): calcula el pago de una membresía.
#
# ============================================================