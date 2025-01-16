#Funciones Lambda
seleccionar = -1

def pedir_numeros():
    try:
        x = int(input("Dime el el primer numero: "))
        y = int(input("Dime el el primer numero: "))
        return [x, y]
    except ValueError:
        print("Valor introducido no valido")


while(seleccionar != 5):
    try:
        seleccionar = int(input("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\n"))

        if(seleccionar == 1):
            numeros = pedir_numeros()
            suma = lambda x, y: x + y
            print(f"La suma es: {suma(numeros[0], numeros[1])}")
        
        elif(seleccionar == 2):
            numeros = pedir_numeros()
            resta = lambda x, y: x - y
            print(f"La resta es: {resta(numeros[0], numeros[1])}")
        
        elif(seleccionar == 3):
            numeros = pedir_numeros()
            multiplicar = lambda x, y: x * y
            print(f"La resta es: {multiplicar(numeros[0], numeros[1])}")
        
        elif(seleccionar == 4):
            try:
                x = int(input("Dime el el primer numero: "))
                y = int(input("Dime el el primer numero: "))
                if(y == 0): raise ZeroDivisionError
                dividir = lambda x, y: x / y
                print(f"La division es: {dividir(x, y)}")

            except ValueError:
                print("Valor introducido no valido")
            except ZeroDivisionError:
                print("La division entre cero no es posible")

    except ValueError:
        print("El valor introducido no es valido")



