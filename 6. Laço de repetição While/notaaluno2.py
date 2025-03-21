import os
os.system("cls||clear")

print("Calculo de média\n")

while True:
    
    nota1 = int(input("Digite sua 1º nota: "))
    nota2 = int(input("Digite sua 2º nota: "))
    nota3 = int(input("Digite sua 3º nota: "))

    if 0 < (nota1 | nota2 | nota3) >10:
     print("Nota inválida(A nota inserida só pode ser maior que zero ou menor que dez).\n")
     
    else:
       media = (nota1 + nota2 +nota3)/3
       if media < 5:
        print(f"Você foi reprovado com média: {media:.1f}")
       elif media >= 5 and media < 7:
        print(f"Você está na recuperação com média: {media:.1f}")
       else:
        print(f"Você foi aprovado com média: {media:.1f}")
       break

print("Programa encerrado.")