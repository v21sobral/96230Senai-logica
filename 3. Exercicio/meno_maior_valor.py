import os
os.system("clear")

numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o primeiro numero: "))
soma = (numero_1 + numero_2)
media = (numero_1 + numero_2)/2
multiplicacao = (numero_1 * numero_2)
sair = str
continuar = str
entrada = input("")

while entrada != "fim":
    if numero_1 > numero_2:
        print(f"O primeiro número que você digitou {numero_1} é o maior número.")
    elif numero_1 == numero_2:
        print(f"Os números: {numero_1} e {numero_2} são iguais.")
    else:
        print(f"O segundo número que você digitou {numero_2} é o maior número.")

    print(f"A soma dos dois números foi: {soma}")
    print(f"A multiplicação dos dois números foi: {multiplicacao:.2f}")
    print(f"A média foi: {media:.2f}")

    entrada = input("Digite sair para encerrar o programa: ")
    numero_1 = float(input("Digite o primeiro numero: "))
    numero_2 = float(input("Digite o primeiro numero: "))
else:
    print("Programa encerrado")
 

