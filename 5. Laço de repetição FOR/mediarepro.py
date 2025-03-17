import os
os.system("clear")
media = 0
for i in range (3):
    nota_1 = float(input("Digite a nota da sua primeira prova: "))
    media += nota_1

if media <= 4:
    print(f"Sua média foi: {media/3:.2f} ")
    print("Reprovado")
elif media >= 5 and media <=7:
    print(f"Sua média foi: {media/3:.2f} ")
    print("Sua nota foi: Nem sei")
else :
    print(f"{media/3:.2f} ")
    print("Nem sei")