import time

tiempo = int(input("Dime el tiempo: "))

for x in range(tiempo, -1, -1):
    time.sleep(1)
    print(x)