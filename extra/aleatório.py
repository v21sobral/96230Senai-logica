import os
os.system("clear")
a = float(input("Digite o número que deseja fazer a exponenciação: "))


match a:
    case 0:
        while a == int :
            b = float(input("Elevado a: "))
            x = (a**b)
            print(f"{a:.0f} elevado a {b:.0f} é igual a {x:.0f}.")
            a = float(input("\nDigite o número que deseja fazer a exponenciação: "))
            b = float(input("Elevado a: "))

        print("Programa encerrado.")