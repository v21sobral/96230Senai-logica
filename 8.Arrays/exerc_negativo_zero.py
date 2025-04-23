import os
os.system("cls||clear")

lista = []

def vetor():
    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número: "))
        if numero < 0:
            numero = 0
        elif numero == 0:
            print("Você digitou o número 0.")
        lista.append(numero)

vetor()
print("Números com negativos igual a 0:", lista)