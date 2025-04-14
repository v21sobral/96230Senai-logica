import os
os.system("cls || clear")

lista_notas = []

for i in range(1, 5):
    nota = float(input(f'Digite a {i}ª nota: '))
    lista_notas.append(nota)

soma = sum(lista_notas)
for nota in lista_notas:
   print(nota)

resultado = soma/i

def aprovacao(resultado):
  if resultado < 5:
     return "Reprovado"
  elif 7 >= resultado > 5:
     return "Recuperação"
  elif resultado >= 7:
     return "Aprovado"
  
classificacao = aprovacao(resultado)
print(f"Média {resultado:.1f}")
print(f"Situação: {classificacao}")
