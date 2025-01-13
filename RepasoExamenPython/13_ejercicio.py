import random
numeroRandom = random.randrange(1, 20)
intentos = 0
nombre = input("Dime tu nombre: ")
print(f"numero random: {numeroRandom}")

respuesta = -1
while(respuesta != numeroRandom):
    respuesta = int(input("Dime tu respuesta: "))

    if(respuesta > numeroRandom):
        print("Muy alto")
    else:
        print("Muy bajo")

    if(intentos == 6): break
    intentos += 1
    print(f"Llevas {intentos} intentos")
    