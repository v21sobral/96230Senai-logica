import os
os.system("cls || clear")


def media_aluno(media):
      media = (nota1 + nota2) / 2
      return media   
      

def aprovacao_aluno(media):
      if media >= 7:
         return "Aprovado"
      
      else:
         return "Reprovado"

nota1 = float(input("Digite a primeira nota: "))
if nota1 > 10:
   print("Nota inválida")  
nota2 = float(input("Digite a segunda nota: "))  
if nota2 > 10:
   print("Nota inválida")      
media = media_aluno(nota1)
aprovacao = aprovacao_aluno(media)
print("\nSaiba a sua média")
print(f"A média do aluno é: {media:.2f}")
print(f"O aluno está: {aprovacao}")
print("\n")
 