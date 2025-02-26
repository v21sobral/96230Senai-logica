import os
os.system("clear")

opcao = int(input("""
Código \t Prato \t\t\t Valor\n
1 \t Picanha \t\t R$ 25,00
_________________________________________
2 \t Lasanha \t\t R$ 20,00
_________________________________________
3 \t Strogonoff \t\t R$ 18,00
_________________________________________
4 \t Bife acebolado \t R$ 15,00
_________________________________________
5 \t Prato feito \t\t R$ 28,00

Digite o código desejado:
"""))


match opcao:
    case 1:
       print("Sua escolha foi: Picanha - R$ 25,00")
    case 2:
       print("Sua escolha foi: Lasanha - R$ 20,00")
    case 3:
       print("Sua escolha foi: - Strogonoff R$ 18,00")
    case 4:
       print("Sua escolha foi: - Bife acebolado R$ 15,00")
    case 5:
       print("Sua escolha foi: - Prato feito R$ 28,00")


print(opcao)