estudiantes = []


seleccionar = -1
while(seleccionar != 0):
    nombre = str(input("Dime el nombre: "))
    edad = int(input("Dime la edad: "))
    calificacion1 = int(input("Dime la primera calificacion: "))
    calificacion2 = int(input("Dime la segunda calificacion: "))
    calificacion3 = int(input("Dime la tercera calificacion: "))
    calificaciones = (calificacion1, calificacion2, calificacion3)

    estudiantes.append({
        "nombre": nombre,
        "edad": edad,
        "calificaciones": calificaciones
    })

    seleccionar = int(input("Para salir presiona 0 si quieres continuar presiona 1: "))




for i in estudiantes:
    sumador = 0
    contador = 0

    print(f"Nombre: {i.get("nombre")}\nEdad: {i.get("edad")}")
    for j in i.get("calificaciones"):
        print(f"Calificacion {contador + 1}: {j}")
        contador += 1
        sumador += j
        
    print(f"Promedio: {sumador/3}")