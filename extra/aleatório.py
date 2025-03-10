import os
os.system("clear")
a = float(input("Digite o número que deseja fazer a exponenciação ou 0 para encerrar o programa: "))

match a:
    case float(0):
        print("Programa encerrado.")
    case a != '0'
        b = float(input("Elevado a: "))
        x = (a**b)
        while a != 0:
            x = (a**b)
            print(f"{a} elevado a {b} é igual a {x}")
            a = float(input("Digite o número que deseja fazer a exponenciação ou 0 para encerrar o programa: "))
            b = float(input("Elevado a: "))
            if a == 0:
                print("Programa encerrado.")
        
             
        