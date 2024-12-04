while(True):
    try:
        edad = int(input("Dime la edad: "))
        if(edad < 0):
            raise ValueError("")
        break
    except:
        print("la edad no es valida")


if(edad < 4):
    print("Entra gratis")
elif(edad > 4 and edad < 18):
    print("Debe pagar 5€")
elif(edad > 18):
    print("Debe pagr 10€")