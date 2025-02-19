import os
os.system("clear")

soma = float
media = float
nota_1 = float(input("Digite a nota da sua primeira prova: "))
nota_2 = float(input("Digite a nota da sua primeira prova: "))
nota_3 = float(input("Digite a nota da sua primeira prova: "))

soma = float((nota_1 + nota_2 + nota_3))
media = float(soma / 3) 

if media >= 7:
    print(f"Sua média foi: {media:.2f} ")
    print("É isso ai mermão, brocou!")
elif media < 3:
    print(f"Sua média foi: {media:.2}f ")
    print("Desista só na próxima encarnação.")
else :
    print(f"{media:.2f} ")
    print("Você é burrão, vá estudar!")


