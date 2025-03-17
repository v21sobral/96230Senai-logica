import os
os.system("cls||clear")
import time

a= int(input("Informe o número para começar a contagem regressiva: "))
print("A contagem regressiva vai começar!\n")
for i in range(a,0,-1):
    print(f" {i}")
    time.sleep(1)

print("Tempo expirado.")