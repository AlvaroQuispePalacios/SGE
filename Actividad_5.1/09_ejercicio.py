import random
import string

print("Generando contraseña")
mayusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
numeros = string.digits
caracterEspecial = string.punctuation
pwd = ""

for i in range(0, 3):
    pwd += random.choice(mayusculas)
    pwd += random.choice(minusculas)
    pwd += random.choice(numeros)
    pwd += random.choice(caracterEspecial)



print(pwd)

