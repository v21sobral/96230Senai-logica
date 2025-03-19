import os
os.system("cls||clear")

contador = 0


while True:
    print("Repitindo...")

    continua = input("Tecle 's' se deseja continuar: ").strip().lower()
    contador += 1

    if continua != 's':
        break

if contador == 0:
    print("O bloco não foi NÃO foi repitido.")
else:
    print(f"O bloco foi repitido {contador} vezes")