

frase = input("Dime una frase: ")

print(f"Frase original: {frase}")
print(f"longitud: {len(frase)}")
print(f"Mayusculas: {frase.upper()} Minusculas: {frase.lower()}")
print(f"Aparece la palabra Python aparece {frase.split(" ").count("Python")} ")
print(f"{frase.replace("a", "@")}")
print(f"{frase.replace("a", "@")}")
print(f"Eliminando los espacios de inicio y final {frase.strip()}")
print(f"Verificando si la palabra programacion esta en la frase utilizando startwith = {frase.startswith("programacion")} y enswith = {frase.endswith("programacion")}")
print(f"{frase[::-1]}")