import os
os.system("cls || clear")

def identificar_par_impar(numero):
    if numero == 0:
        return "Nem par, nem ímpar."
    elif numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = int(input("Digite um número para saber se é par/ímpar: "))

# Chama a função e exibe o resultado
resultado = identificar_par_impar(numero)
print(f"o número {numero} é: {resultado}")