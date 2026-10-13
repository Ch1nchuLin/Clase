import time
import random



def cochinada(nombre, contra, condicion):
    
    if(nombre =="pepito" and contra ==1234):
        for i in range (10):
            print("Pepito puto " + str(random.randint(10,100)) + " " + str(random.randint(10,100)))
            time.sleep (0.5)
            print()
    else:
        print ("Usuario o contrasena incorrectos")

cochinada(nombre = "pepito", contra = 1234, condicion = True)

def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        sequence.append(b)
    return sequence

# Example usage:
print(fibonacci_iterative(15))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]



