#Listas
    
#indices:   #0        #1      #2
nombres = ["Juanito","Pepito","Anito"]

            #0     #1   #2    #3
precios = [20.50,30.55,69.67,88.93]

for i in range(1):
    print(f"Precio del producto precios ${precios[2]}")

def sumar (*numeros):
    #argumentos args son itpo tupla
    print(type(numeros))
    total = 0
    for numero in numeros:
        total+=numero
    return total

print(sumar(2,3,4,5,6))

utiles = ["borrador","sacapunta","tijeras","cuadernos",
          "lapices","regla","lapicero","plumones"]

#Slice con dos limites
print(utiles[1:5])
#Slice con limite superior
print(utiles[:4])
#Slice con limite inferior
print(utiles[3:])
#Slice que imprime toda la lista
print(utiles[:])

print(utiles+nombres)

print("escuadra" not in utiles)

#Append agrega a la lista
nombres.append("Maria")
print(nombres)

#insert + ubicacion en el indice
utiles.insert(2,"compas")
print(utiles)

#pop
precios.pop()
print(precios)

#remove
utiles.remove("cuadernos")
print(utiles)

#sort
utiles.sort()
print(utiles)

#sort con numeros lo hace de manera ascendente
precios.sort()
print(precios)

#sort con numeros desencentes 
precios.sort(reverse=True)
print(precios)

utiles.sort(key=len)
print(utiles)

