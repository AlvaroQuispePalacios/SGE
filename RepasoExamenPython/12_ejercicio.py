lista = []
tamanyoLista = int(input("Dime cuantos numeros quieres ingresar: "))
sumador = 0

for i in range(0, tamanyoLista):
    numero = int(input("Dime un numero: "))
    sumador += numero
    lista.append(numero)


print(f"El promedio es: {sumador/len(lista)}")
