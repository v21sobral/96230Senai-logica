import os
os.system("cls || clear")

lista_notas = []

for i in range(1, 4):
    nota = float(input(f'Digite a {i}ª nota: '))
    lista_notas.append(nota)

soma = sum(lista_notas)
for nota in lista_notas:
   print(nota)

resultado = soma/i
print(f"Média: {resultado:.1f}")