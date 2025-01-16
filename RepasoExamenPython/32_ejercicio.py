#Argumentos arbitrarios
tupla = ("matematicas", "letras")
diccionario = {
    "nombre": "Alvaro",
    "edad": 23,
    "ciudad": "Alaior" 
}

def registrar_estudiante(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}")


registrar_estudiante(nombre = "Alvaro", edad = 23, ciudad = "Alaior")