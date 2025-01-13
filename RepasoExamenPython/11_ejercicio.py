edad = int(input("Dime la edad: "))
if(edad < 4):
    print("Entra gratis")
elif(edad >=4 and edad <=18):
    print("Paga 5€")
elif(edad > 18):
    print("Paga 10€")