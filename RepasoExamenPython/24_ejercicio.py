import random
seleccionar = -1
lista = []
while(seleccionar != 7):
    seleccionar = int(input("1. Crear una lista\n2. Mostrar lista\n3. Mostrar mayor numero de la lista\n4. Mostrar menor numero de la lista\n5. Sumar numeros de la lista\n6. Calcular promedio de la lista\n7. Salir\n"))

    if(seleccionar == 1):
        for i in range(0, 5):
            lista.append(random.randrange(1, 20))
        print(lista)
    
    elif(seleccionar == 2):
        if(len(lista) != 0):
            print(lista)

        else:
            print("La lista no ha sido creada")
    
    elif(seleccionar == 3):
        if(len(lista) != 0):
            print(max(lista))

        else:
            print("La lista no ha sido creada")

    elif(seleccionar == 4):
        if(len(lista) != 0):
            print(min(lista))

        else:
            print("La lista no ha sido creada")
    
    elif(seleccionar == 5):
        if(len(lista) != 0):
            sumador = 0
            for i in lista:
                sumador += i
            
            print(f"La suma de la lista es: {sumador}")

        else:
            print("La lista no ha sido creada")
    
    elif(seleccionar == 6):
        if(len(lista) != 0):
            sumador = 0
            for i in lista:
                sumador += i
            
            print(f"El promedio es: {sumador/len(lista)}")
            
        else:
            print("La lista no ha sido creada")