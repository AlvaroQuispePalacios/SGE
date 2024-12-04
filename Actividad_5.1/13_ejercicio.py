import random

intentos = 0
numeroRandom = random.randrange(20)
ganado = False
print(numeroRandom)
while(ganado != True):
    print("ADIVINA EL NUMERO")
    numero = int(input("Dime un numero: "))

    if(numero < numeroRandom):
        print("Muy bajo")
        intentos += 1
        print(f"Intentos: {intentos}")
    elif(numero > numeroRandom):
        print("Muy Alto")
        intentos += 1
        print(f"Intentos: {intentos}")
    elif(numero == numeroRandom):
        ganado = True

print("GANASTE")