contador = 0

def decorador(func):
    def envoltura(nombre, contador):
        contador += 1
        func(nombre)
    print(contador)
    return envoltura


@decorador
def llamar_funcion(nombre):
    print(f"Hola {nombre}")

llamar_funcion("Alvaro", contador)
llamar_funcion("Pedro", contador)
