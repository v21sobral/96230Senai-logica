import os
os.system("cls || clear")


def positivo_negativo(numero):
    if numero > 0:
        return "Positivo"
    else:
        return "Negativo"


numero = int(input("Digite um número para saber se é par/ímpar: "))

# Chama a função e exibe o resultado
resultado = positivo_negativo(numero)
print(f"o número {numero} é: {resultado}")