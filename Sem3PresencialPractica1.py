#Realizar un codigo que gestione una tienda, la tienda debe pode:
#Ingresar un producto, Ver los productos en cualquier momento, Todo se manejara por un menu que funionara
#En bucle hata que el usuario salga por complet
#Se tiene que poder regresar al menu principa;
#Ejm: Menu
# 1-Ingresar producto
# 2-Ver Inventario
# 3-Salir

inventario = [("ID001","Lapicero",50),
              ("ID002","Cuaderno",20)]
print("****************************")
print("**[Tienda Tung Tung Sahur]**")
print("****************************")

while True:
    
    opcion = input("Que desea hacer?\n" +
                   f"# 1-Ingresar prodcuto \n"+ 
                   f"# 2-Ver Inventario \n" +
                   f"# 3-Salir \n")
    if (opcion == '1'):
            nuevocod = input("Ingrese el codigo de el producto: ")
            nuevonom = input("Ingrese el nombre del prodcuto: ")
            nuevostock = int(input("Ingresa el stock del prodcto: "))
            nuevoprod = (nuevocod,nuevonom,nuevostock)
            inventario.append(nuevoprod)
    elif (opcion == '2'):
          nprod = 12
          for codigo,nombre,stock in inventario:
            print("***********************")
            print(f"{nprod}*"+
                f"Codigo ---------- {codigo}\n"+ 
                f"Nombre ---------- {nombre}\n"+
                f"Stock  ---------- {stock}\n")
            print("***********************")
            nprod+=1
    elif (opcion == '3'):
          print("Gracias por comprar en tienda Tung Tung Sahur")
          break
    else:
          print("Ingrese un numero valido para la operacion")
          continue