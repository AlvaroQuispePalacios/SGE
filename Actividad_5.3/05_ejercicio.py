
seleccionar = -1

def pedir_numeros():
    try:
        x = int(input("Dime el primer numero: "))
        y = int(input("Dime el segundo numero: "))
        return [x, y]
    except ValueError:
        print("La entrada no es valida")
    

while(seleccionar != 5):
    seleccionar = int(input("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\n"))

    if(seleccionar == 1):
        numeros = pedir_numeros()
        suma = lambda x, y: x + y
        print(f"Suma: {suma(numeros[0], numeros[1])}")
    
    elif(seleccionar == 2):
        numeros = pedir_numeros()
        resta = lambda x, y: x - y
        print(f"Resta: {resta(numeros[0], numeros[1])}")

    elif(seleccionar == 3):
        numeros = pedir_numeros()
        multiplicar = lambda x, y: x * y
        print(f"Multiplicar: {multiplicar(numeros[0], numeros[1])}")

    elif(seleccionar == 4):
        try:
            x = int(input("Dime el primer numero: "))
            y = int(input("Dime el segundo numero: "))
            if(y == 0): raise ZeroDivisionError
            dividir = lambda a, b: a/b
            print(f"Dividir: {dividir(x, y)}")
        except ValueError:
            print("La entrada no es valida")
        except ZeroDivisionError:
            print("La division por cero no es posible")



