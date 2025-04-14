import os
os.system("cls || clear")

lista_numero = []
print("DIGITE SEUS NÚMEROS")
for i in range(1, 6):
    numero = float(input(f'Digite o {i}ª número: '))
    lista_numero.append(numero)

lista_numero.reverse()
for i, numero in  enumerate(lista_numero,start=1):
    print(f"{i}º número: {numero}")

numero_maior = max(lista_numero)
numero_menor = min(lista_numero)


print(" ")
print(f"Maior número: {numero_maior}")
print(f"Menor número: {numero_menor}")



