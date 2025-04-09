import os
os.system("cls || clear")

def conversor(numero):
    return numero * 100

         

numero = float(input("Digite o número que deseja converter em cm: "))
convert = conversor(numero)
print(f"{numero}m = {convert:.2f}cm")