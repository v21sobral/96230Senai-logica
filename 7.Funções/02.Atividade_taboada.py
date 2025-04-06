import os
os.system("cls || clear")
import time

def taboada(numero):
    resultados = 
    for i in range(11):
        resultados += f"{numero} x {i} = {numero * i}\n"
    return resultados
    

numero = int(input("Digite um número para saber sua tabuada: "))
mostra_taboada = taboada(numero)

print(f"Tabuada do número: {numero}")
print(mostra_taboada)