frase = input("Dime una : ")

print(frase)
print(f"La longitud de la frase es: {len(frase.strip())}")
print(f"Mayus : {frase.upper()} Minus: {frase.lower()}")

print(f"La palabra Python aparece: {frase.count("Python")}")

print(f"{frase.replace("a", "@")}")
# strip() --> Elimina un caracter en el principio y final por defecto son los espacios
print(frase.strip())
print("")
# Ternario
print(f"La palabra programacion {"si esta" if frase.startswith("programacion") or frase.endswith("programacion") else "no esta"}")
# La reversed()función devuelve un objeto iterador que proporciona acceso a los elementos de un iterable (lista, tupla, cadena, etc.) en orden inverso.
print("".join(list(reversed(frase))))
print(frase.title())
