import os
os.system("cls||clear")

print("Programa par/ímpar.")
numero = 0
soma_pares = 0
contador = 0
quantidade_impar = 0
quantidade_par = 0
soma_geral = 0

while True:
  numero = int(input("Digite o número:"))
 
  if numero == 0:
    break
 
  if numero % 2 == 0:
    quantidade_par += 1
    soma_pares += numero
  else:
    quantidade_impar += 1


contador += 1
soma_geral += numero

media_pares = soma_pares / quantidade_par
media_geral = soma_geral / contador

print(f"\nQuantidade e pares: {quantidade_par}")
print(f"\nQuantidade e ímpares: {quantidade_par}")
print(f"\nMédia pares: {media_pares}")
print(f"\nMédia geral: {media_geral}")

   
   
   

         