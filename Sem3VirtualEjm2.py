#Tuplas/Tuples
# ()
# Tienen indices y son inmutables 

depts = ("San miguel", "Usulutan", "Morazan", "La Union")

print(depts.count("San miguel"))
print(depts.index("Morazan"))
print(depts[0])

def sumar (*numeros):
    #argumentos args son itpo tupla
    print(type(numeros))
    total = 0
    for numero in numeros:
        total+=numero
    return total

print(sumar(2,3,4,5,6))
