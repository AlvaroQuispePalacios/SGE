array = []
seleccionar = -1
while(seleccionar != 0):
    numero = int(input("Dime un numero: "))
    if(numero == 0):
        seleccionar = 0
    else:
        array.append(numero)


array.sort()
print(f"Array ascendente: {array}")

array.sort(reverse=True)
print(f"Array descendente: {array}")
