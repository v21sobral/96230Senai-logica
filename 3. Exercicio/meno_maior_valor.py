import os
os.system("clear")

numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o primeiro numero: "))
soma = (numero_1 + numero_2)
media = (numero_1 + numero_2)/2
multiplicacao = (numero_1 * numero_2)



if numero_1 > numero_2:
    print(f"Esse é o maior número: {numero_1}")
else:
    print(f"Esse é o maior número: {numero_2}")

print(f"A soma dos dois números foi: {soma}")
print(f"A multiplicação dos dois números foi: {multiplicacao}")
print(f"A média foi: {media:.2f}")

 

