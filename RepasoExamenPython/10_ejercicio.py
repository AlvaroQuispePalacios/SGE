
x = int(input("Dime un numero: "))
y = int(input("Dime un numero: "))

operacion = input("Selecciona la operacion:\n1. +\n2. -\n3. *\n4. /\n")

if(operacion == "+"):
    print(f"La suma es: {x + y}")
elif(operacion == "-"):
    print(f"La resta es: {x - y}")
elif(operacion == "*"):
    print(f"La multiplicacion es: {x * y}")
elif(operacion == "/"):
    if(y == 0):
        print("La division entre cero no es posible")
    else:
        print(f"La division es: {x / y}")    



