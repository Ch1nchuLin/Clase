#Ejm1
#Tienda necesita registrar prodctos, cada producto tiene nombre y stock
#El Stock puede cambiar

inventario = [("ID001","Lapicero",50),
              ("ID002","Cuaderno",20)]

print("***Ingreso de nuevo producto***")

while True:

    nuevocod = input("Ingrese el codigo de el producto: ")
    nuevonom = input("Ingrese el nombre del prodcuto: ")
    nuevostock = int(input("Ingresa el stock del prodcto: "))
    nuevoprod = (nuevocod,nuevonom,nuevostock)
    inventario.append(nuevoprod)

    opcion = input("Desea ingresar otro producto? (s/n)").strip().lower()
    if (opcion == 's'):
        continue
    else:
        break


print("**Inventario actual**")
nprod = 1
for codigo,nombre,stock in inventario:
    print(f"{nprod}*"+
          f"Codigo ---------- {codigo}\n"+ 
          f"Nombre ---------- {nombre}\n"+
          f"Stock  ---------- {stock}\n")
    print("***********************")
    nprod+=1