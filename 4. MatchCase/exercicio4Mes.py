import os
os.system("clear")



numero = int(input("""
1 -\t Janeiro
2 -\t Fevereiro
3 -\t Março 
4 -\t Abril  
5 -\t Maio                  
6 -\t Junho                 
7 -\t Julho
8 -\t Agosto
9 -\t Setembro
10 -\t Outubro
11 -\t Novembro
12 -\t Dezembro
                   
Digite o número do mês desejado:                                   
"""))


match numero:
    case 1:
        print(f"Você escolheu Janeiro.")
    case 2:
        print("Você escolheu Fevereiro.")
    case 3:
        print("Você escolheu Março.")
    case 4:
        print("Você escolheu Abril.")
    case 5:
        print("Você escolheu Maio.")
    case 6:
        print("Você escolheu Junho.")
    case 7:
        print("Você escolheu Julho.")
    case 8:
        print("Você escolheu Agosto.")
    case 9:
        print("Você escolheu Setembro.")
    case 10:
        print("Você escolheu Outubro.")
    case 11:
        print("Você escolheu Novembro.")
    case 12:
        print("Você escolheu Dezembro.")
    case _:
        print("Mês inválido!")