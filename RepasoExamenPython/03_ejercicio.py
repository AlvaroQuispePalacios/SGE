nombre = input("Dime tu nombre completo: ")
setearNombre = nombre.strip().lower().split()
email = ".".join(setearNombre) + "@iesjoanramis.org"
print(email)