import os
os.system("cls || clear")

#Criando uma lista
lista_notas = []

#Adicionando  3 notas em uma lista
for i in range(3):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    lista_notas.append(nota)

#Exibindo todos os valores em uma lista
print()
for nota in lista_notas:
    print(nota)

