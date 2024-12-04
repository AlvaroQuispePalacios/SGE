numero = int(input("Dime un numero positivo: "))
arrayNumeros = []
while(numero < 100):
    if(numero > 0):
        arrayNumeros.append(numero)

    numero = int(input("Dime otro positivo: "))

print("Los numeros son")
for i in arrayNumeros:
    print(i)