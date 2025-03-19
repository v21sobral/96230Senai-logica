import os
os.system("cls||clear")



while True:
    nota1 = int(input("Digite sua 1º nota: "))
    nota2 = int(input("Digite sua 2º nota: "))

    if nota1 <0 or nota1 >10:
     print("1º nota inválida.\n")
    elif nota2 <0 or nota2 >10:
     print("2º nota inválida.\n")
    else:
       print(f"Sua média foi: {(nota1 + nota2)/2}")
       break

print("FIM")