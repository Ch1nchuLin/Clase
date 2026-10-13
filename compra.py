NombreProd = (input("Ingrese el nombre de el producto: "))
CantidadProd = float((input("Ingrese la cantidad de el producto: ")))
PrecioPrdo = float((input("Ingrese precio de el producto: ")))

costo = CantidadProd * PrecioPrdo

Total = print("El precio total de " + NombreProd + " es: " + str(costo + (costo*0.13)))
