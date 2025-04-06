import os
os.system("cls || clear")

def identificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = int(input("Digite um número para saber se é par/ímpar: "))

# Chama a função e exibe o resultado
resultado = identificar_par_impar(numero)
print(f"o número {numero} é: {resultado}")