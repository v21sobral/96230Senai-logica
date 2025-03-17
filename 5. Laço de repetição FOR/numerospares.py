import os
os.system("cls||clear")
import time

print("Digite 5 médias para saber o resultado final.")
soma = 0
for i in range(5):
    nota = float(input(f"Digite a {i+1}º nota : "))
    #soma = soma + nota ou
    soma += nota

print(f"A soma deu: {soma}")
    
    

print("Já foi!")

