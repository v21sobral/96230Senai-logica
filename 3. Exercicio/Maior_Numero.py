import os
os.system("clear")


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

menor = min(numero1,numero2)
maior = max(numero1,numero2)

print("\nDigite dois números para saber qual o maior deles dois:")
print(f"Os número digitados foram: {numero1:.2f} e {numero2:.2f}")
if numero1 == numero2:
    print("Os números são iguais.")
else:
    print(f"\nO maior número foi: {maior:.2f}  Menor número foi: {menor:.2f}")
    print("\n")
    