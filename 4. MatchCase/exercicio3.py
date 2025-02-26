import os
os.system("clear")

numero = int(input("""
1 -\t Domingo
2 -\t Segunda-feira
3 -\t Terça-feira 
4 -\t Quarta-feira  
5 -\t Quinta-feira                  
6 -\t Sexta feira                  
7 -\t Sábado
                   
Digite o número do dia desejado:                                   
"""))

match numero:
    case 1:
        print("Domingo")
    case 2:
        print("Você escolheu segunda-feira.")
    case 3:
        print("Você escolheu Terça-feira.")
    case 4:
        print("Você escolheu Quarta-feira.")
    case 5:
        print("Você escolheu Quina-feira.")
    case 6:
        print("Você escolheu Sexta-feira.")
    case 7:
        print("Sábado")
    case _:
        print("Dia inválido!")

if numero == 1 or numero == 7:
    print("O dia escolhido é um final de semana.")
if numero >= 2 and numero <=6:
    print("O dia escolhido é um dia de semana normal.")

