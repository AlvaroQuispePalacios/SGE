x = int(input("Dime un numero: "))
esPrimo = True
for n in range(2, x):
    if(x % n == 0):
        esPrimo = False
    break

if(esPrimo):
    print("el numero es primo")
else:
    print("el numero no es primo")
    