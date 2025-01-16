lista = []

try:
    tamanyoLista = int(input("Dime el tamaño de la lista: "))
    for i in range(0, tamanyoLista):
        valor = int(input("Dime los elementos de la lista: "))
        lista.append(valor)
except ValueError:
    print("La lista solo acepta numeros")

def mostrar_lista(lista):
    print(lista)

def insertar_elemento(lista, posicion, valor):
    lista[posicion] = valor

def eliminar_elemento(lista, posicion):
    del lista[posicion]

def ordenar_lista(lista):
    lista.sort()

seleccionar = -1 
while(seleccionar != 5):
    try:
        seleccionar = int(input("1. Mostrar lista actual\n2. Insertar elemento en una posición especifica\n3. Eliminar un elemento por posición\n4. Ordenar la lista de manera ascendente\n5. Salir\n"))

        if(seleccionar == 1):
            mostrar_lista(lista)
        
        elif(seleccionar == 2):
            # Pide la posicion y luego verifica que la posicion se encuentra entre 0 y el tamaño de la lista, si la posicion es valida inserta el nuevo elemento
            posicion = int(input("Dime la posicion que quieres insertar el nuevo elemento: "))
            if(posicion < len(lista) and posicion >= 0):
                valorNuevo = int(input("Dime el nuevo valor: "))
                insertar_elemento(lista, posicion, valorNuevo)
            else:
                print("La posicion no es valida")
        
        elif(seleccionar == 3):
            posicion = int(input("Dime la posicion del elemento que quieres eliminar: "))
            if(posicion < len(lista) and posicion >= 0):
                eliminar_elemento(lista, posicion)
            else:
                print("La posición no es valida")

        elif(seleccionar == 4):
            ordenar_lista(lista)
            print(lista)

    except ValueError:
        print("Valor introducido no es valido")