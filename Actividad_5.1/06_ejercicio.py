sumador = 0
numero = int(input("Dime un numero: "))
while(numero != 0):
    sumador += numero
    numero = int(input("Dime un numero: "))

print(f"La suma es: {sumador}")