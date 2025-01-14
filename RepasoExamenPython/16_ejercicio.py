lista1 = []
lista2 = []

for i in range(1, 6):
    lista1.append(i)

print(lista1)
for i in range(6, 11):
    lista2.append(i)
print(lista2)

lista2.extend(lista1)
print(lista2)

