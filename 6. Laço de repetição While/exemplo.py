import os
os.system("cls||clear")

contador = 0
continua = 's'

while continua == 's':
    print("Repitindo...")

    contador += 1

    continua = input("Tecle 's' se deseja continuar: ").strip().lower()

if contador == 0:
    print("O bloco não foi NÃO foi repitido.")
else:
    print(f"O bloco foi repitido {contador} vezes")

