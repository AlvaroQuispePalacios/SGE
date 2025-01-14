lista = []
numero = -1
while(numero != 0):
    numero = int(input("Dime un numero: "))
    lista.append(numero)

lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
