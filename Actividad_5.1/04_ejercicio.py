nombre = input("Dime tu nombre: ")
numero = input("Dime un numero: ")

for i in range (0, int(numero)):
    print(nombre)
    print(f"{nombre} numero de letras {len(nombre)}")