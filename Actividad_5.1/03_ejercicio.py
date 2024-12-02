nombre = input("Dime tu nombre completo: ")

inicioEmail = nombre.strip().lower().split(" ")
email = ".".join(inicioEmail) + "@iesjoanramis.org"
print(email)
