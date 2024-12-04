numeros = []
numeroValido = False
sumador = 0

while(numeroValido == False):
    tamanyoArray = int(input("Dime el tamaño del array: "))
    if(tamanyoArray < 0):
        print("El tamaño del array no es valido")
    elif(tamanyoArray > 0):
        numeroValido = True

for i in range(0, tamanyoArray):
    numeros.append(int(input("Dime un numero: ")))

for i in range(0, tamanyoArray):
    sumador += numeros[i]

print(sumador)