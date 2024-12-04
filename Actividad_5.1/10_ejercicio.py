def elegirYComprobarNumero():
    while(True):
        try:
            x = int(input("Dime un numero: "))
            return x
        except:
            print("El numero introducido no es valido")

x = elegirYComprobarNumero()
y = elegirYComprobarNumero()


def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicar(x, y):
    return x * y 

def dividir(x, y):
    try:
        return x/ y
    except:
        return "la division no es valida"
    
operacion = str(input("Elige una de las opciones\n+ \n- \n* \n/ \n"))

if(operacion == "+"):
    print(f"resultado: {suma(x, y)}")

elif(operacion == "-"):
    print(f"resultado: {resta(x, y)}")

elif(operacion == "*"):
    print(f"resultado: {multiplicar(x, y)}")

elif(operacion == "/"):
    print(f"resultado: {dividir(x, y)}")
else:
    print("No se ha seleccionado ninguna de las operaciones")





