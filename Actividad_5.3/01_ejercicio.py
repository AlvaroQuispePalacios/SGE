def registrar_asignatura(*args):
    print("Asignaturas: ")
    for asignatura in args:
        print (asignatura)
    

def registrar_estudiante(**kwargs):
    print("Datos estudiante:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


registrar_estudiante(nombre="Alvaro", edad=23, ciudad="Alaior")
registrar_asignatura("filosofia", "matematicas")
print("\n")
registrar_estudiante(nombre="Pedro", edad=19, ciudad="Alaior")
registrar_asignatura("Aritmetica", "matematicas")