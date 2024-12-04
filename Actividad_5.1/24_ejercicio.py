import random
seleccionar = -1
numerosAleatorios = []

while(seleccionar != 7):
    seleccionar = int(input("1. Crear nueva lista\n2. Ver lista\n3. Mostrar el mayor numero\n4. Mostrar el menor numero\n5. Sumar numeros de la lista \n6. Calcular promedio de la lista \n7. Salir\n"))

    if(seleccionar == 1):
        for i in range(0, 10):
            numerosAleatorios.append(random.randint(1, 100))
    elif(seleccionar == 2):
        if(len(numerosAleatorios) == 0):
            print("La lista no existe")
        else:
            print(numerosAleatorios)
    elif(seleccionar == 3):
        if(len(numerosAleatorios) == 0):
            print("La lista no existe")
        else:
            print(f"El numero mayor de la lista es: {max(numerosAleatorios)}\n")
    elif(seleccionar == 4):
        if(len(numerosAleatorios) == 0):
            print("La lista no existe")
        else:
            print(f"El numero menor de la lista es: {min(numerosAleatorios)}\n")
    elif(seleccionar == 5):
        if(len(numerosAleatorios) == 0):
            print("La lista no existe")
        else:
            sumador = 0
            for i in numerosAleatorios:
                sumador += i
            print(f"La suma de todos los elementos de la lista es: {sumador}")
    elif(seleccionar == 6):
        if(len(numerosAleatorios) == 0):
            print("La lista no existe")
        else:
            sumador = 0
            for i in numerosAleatorios:
                sumador += i
            print(f"El promedio es: {sumador/len(numerosAleatorios)}")