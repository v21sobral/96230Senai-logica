import os
os.system("cls")

print("Informe o número para saber sua taboada.")

numero1=int(input("Digite o número que você deseja sabe a taboáda:"))
for i in range (11):
    print(f"A taboáda do número: {numero1} ")
    print(f"{numero1} * {i} = {numero1 * i}")