# POO

class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if(self.saldo > cantidad):
            self.saldo -= cantidad
        else:
            print("No se puede retirar esta cantidad")

    def mostrar_informacion(self):
        print(f"Titular: {self.titular}\nSaldo: {self.saldo}")


persona = CuentaBancaria("Alvaro")
persona2 = CuentaBancaria("Aldo")

persona.mostrar_informacion()
persona2.mostrar_informacion()

persona.depositar(2000)
persona.retirar(1500)
persona2.retirar(1000)
persona2.depositar(700)

persona.mostrar_informacion()
persona2.mostrar_informacion()