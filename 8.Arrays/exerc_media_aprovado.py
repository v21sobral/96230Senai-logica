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


if resultado < 5:
  print(f"Média: {resultado:.1f}" " " "Reprovado")
elif 7 >= resultado > 5:
  print(f"Média: {resultado:.1f}" " " "Recuperação")
elif resultado > 7:
  print(f"Média: {resultado:.1f}" " " "Aprovado")