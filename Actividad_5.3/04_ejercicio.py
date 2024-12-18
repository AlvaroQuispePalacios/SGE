class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo += cantidad 

    def retirar(self, cantidad):
        if(self.saldo >= cantidad):
            self.saldo -= cantidad
        else:
            print("La cantidad a retirar es mayor que el saldo")
        
    def mostrar_informacion(self):
        print(f"Titular: {self.titular}\nSaldo: {self.saldo}")

cuentaBancaria1 = CuentaBancaria("Alvaro")
cuentaBancaria2 = CuentaBancaria("Pedro")


cuentaBancaria1.mostrar_informacion()
cuentaBancaria2.mostrar_informacion()

cuentaBancaria1.retirar(200)
cuentaBancaria1.depositar(400)

cuentaBancaria2.depositar(700)
cuentaBancaria2.retirar(200)

cuentaBancaria1.mostrar_informacion()
cuentaBancaria2.mostrar_informacion()