import os
os.system("cls||clear")

media = 0
for i in range (4):
    nota = float(input(" Digite suas notas: "))
    media += nota

print(f"Sua média é: {media / 4}")
