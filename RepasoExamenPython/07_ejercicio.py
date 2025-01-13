seleccionar = -1
sumador = 0

while(seleccionar < 100):
    seleccionar = int(input("Dime un numero: "))
    if(seleccionar > 0 and seleccionar < 100 ):
        sumador += seleccionar
    

print(sumador)