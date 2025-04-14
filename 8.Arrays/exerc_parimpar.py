import os
os.system("cls || clear")
contadorpar = 0
contadorimpar = 0
lista_numero = []
print("DIGITE SEUS NÚMEROS")
for i in range(1, 7):
    numero = int(input(f'Digite o {i}ª número: '))
    lista_numero.append(numero)
def pares_impares(lista):
    for i, numero in  enumerate(lista_numero,start=1):
        if numero == 0:
            print(f"{numero} não é par nem ímpar.")
        elif numero % 2 == 0:
            contadorpar += 1
            return "é par"
        elif numero % 2 != 0:
            contadorimpar += 1
            return "é par"

print("")
print(f"Numéro pares: {contadorpar}")
print(f"Numéro impares: {contadorimpar}")










