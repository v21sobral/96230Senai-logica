import os
os.system("cls || clear")


def positivo_negativo(numero):
    if numero > 0:
       print(f"O numero {numero} é positivo")
    elif numero == 0:
       print(f"O número {numero} é neutro.")
    else:
       print(f"O numero {numero} é negativo")
        

numero = int(input("Digite um número para saber se o número é positivo/negativo: "))
resultado = positivo_negativo(numero)
