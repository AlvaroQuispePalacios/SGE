#Decorador medir tiempo
import time

def decorador(func):
    def envoltura():
        print("Antes de ejecutar la funcion")
        ti = time.time()
        func()
        tf = time.time()

        tr = tf-ti
        print(round(tr))

    return envoltura


@decorador
def sumarNumeros():
    return (10000000000 * (10000000000 + 1))/2


sumarNumeros()

# import time

# def medir_tiempo(func):
#     def envoltura(numero):
#         print("Antes de ejecutar la función...")
#         inicio = time.time()  # Inicia el cronómetro
#         resultado = func(numero)  # Ejecuta la función
#         fin = time.time()  # Finaliza el cronómetro
#         print(f"La función tomó {fin - inicio:.6f} segundos en ejecutarse.")
#         return resultado  # Devuelve el resultado de la función
#     return envoltura

# @medir_tiempo
# def sumarNumeros(numero):
#     return (numero * (numero + 1)) / 2

# # Llamada a la función decorada
# resultado = sumarNumeros(1000000)
# print(f"Resultado: {resultado}")
