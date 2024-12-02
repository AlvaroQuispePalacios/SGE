x = input("Dime un numero positivo mayor que 2: ")
x_int = int(x)
esPrimo = True

if(type(x_int) == int and x_int > 2):
    print(f"El numero es {x}")
    for i in range(2, x_int):
        if x_int % i == 0:
            esPrimo = False
            break


if(esPrimo):
    print("Es primo")
else:
    print("No es primo")
