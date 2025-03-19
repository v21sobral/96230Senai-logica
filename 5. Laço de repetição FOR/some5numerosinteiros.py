import os
os.system("cls||clear")
import time

print("Digite 5 médias para saber o resultado final.")
pares = 0
impares = 0
for valor in range(5):
    valor = float(input(f"Digite o {valor+1}º valor : "))
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1


print(f"\nVocê tem: {pares} pares.")
print(f"Você tem:{impares} é par.")

    
    

print("Já foi!")
