lista1 = []
lista2 = []
for i in range(1, 6):
    lista1.append(i)

for i in range(6, 11):
    lista2.append(i)

lista1.extend(lista2)

print(lista1)
lista1.reverse()
print(lista1)
