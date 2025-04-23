import os
os.system("cls || clear")
lista_numero = []
QUANTIDADE_NUMERO = 6
print("DIGITE SEUS NÚMEROS")
contadorpar = 0
contadorimpar = 0
nemparnemimpar = 0

for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f'Digite o {i+1}ª número: '))
    lista_numero.append(numero)

def pares_impares(lista):
    contadorpar = 0
    contadorimpar = 0
    nemparnemimpar = 0
    for i, numero in enumerate(lista, start=1):
        if numero == 0:
            nemparnemimpar += 1
        elif numero % 2 == 0:
            contadorpar += 1
        elif numero % 2 != 0:
            contadorimpar += 1
    return contadorpar, contadorimpar, nemparnemimpar

contadorpar, contadorimpar, nemparnemimpar = pares_impares(lista_numero)

print("")
print(f"Números pares: {contadorpar}")
print(f"Números ímpares: {contadorimpar}")
print(f"Números nem pares e nem ímpares: {nemparnemimpar}")










