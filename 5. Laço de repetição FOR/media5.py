import os
os.system("cls||clear")
print("Digite suas notas para saber sua média final.\n")
media = 0
for nota in range (4):
    nota = float(input(f" Digite suas {nota + 1}º nota: "))
    media += nota

print(f"Sua média é: {media / 4}")
